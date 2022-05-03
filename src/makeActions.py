from turtle import position
import pyautogui as gui
from superAutoPetsPositions import *
import time 
class movingPets():
    def __init__(self, input):
        self.team = input 
    
    def move(self, current, destination):
        '''
        the sub team can move left or right
        '''
        if current == destination:
            return self.team 
        if current < destination:
            temp = self.team[current]
            for i in range(current-destination):
                self.team[current+i] = self.team[current+i+1]
            self.team[destination] = temp
            return  self.team 
        else:
            temp = self.team[current]
            for i in range(current - destination):
                self.team[current - i] = self.team[current - i - i]
            self.team[destination] = temp
            return self.team 
    
class SuperAutoPetsMouse():
    '''
    A Class that implements the interface between reinforcement agent and game
    convention: 
        - when the parameters for a method has 2 inputs(team slot, shop slot) then the team slot
        always comes in the first
    '''
    def __init__(self):
        self.position = get_position() 
        self.team_position = [1]*5

    def _shop2team(self, n1, n2):
        '''
        helper method to click to locations 
        '''
        gui.click(self.position[str(n1)+'_slot'])
        gui.click(self.position[str(n2)+'_team_slot'])

    def _click(self, first_click):
        '''
        helper method to click
        '''
        gui.click(self.position[first_click])
    
    def _movePet(self, n1, n2):
        '''
        a helper method to move the pets in the team
        n1 to n2
        '''
        if n1 == n2:
            return

        self._click(str(n1)+'_team_slot')
        gui.mouseDown(button="left")
        gui.moveTo(self.position[str(n2)+'_team_slot'][0],
        self.position[str(n2)+'_team_slot'][1], duration=1)
        time.sleep(3)
        gui.mouseUp(button="left")



    def buy(self, nth_slot):
        '''
        method to buy pets from shop
        '''
        print(nth_slot)
        if len(nth_slot) == 2:
            nth_slot1 = nth_slot[0]
            nth_slot2 = nth_slot[1]
            self._shop2team(nth_slot1, nth_slot2)
            return 
        nth_slot = nth_slot[0]
        for j,i in enumerate(self.team_position):
            if i:
                self._shop2team(nth_slot, j+1)
                self.team_position[j] = 0
                return
    
    def buy_food(self, nth_slot, target=3):
        '''
        method to buy food
        '''
        if nth_slot == 5 or nth_slot == 6: 
            self._shop2team(nth_slot, target)

    def sell_buy(self,nth_slot, nth_team_slot):
        '''
        method to buy and place the pet in a specified team slot
        '''
        if self.team_position[nth_team_slot - 1] == 0:
            self.sell(nth_team_slot)
            self._shop2team(nth_slot, nth_team_slot)
            self.team_position[nth_team_slot - 1] = 0
        else:
            raise Exception("Invalid sell_buy: No pet present in the slot to buy...")
            
    def sell(self, nth_team_slot):
        '''
        method to sell a pet from the team
        '''
        if self.team_position[nth_team_slot - 1] == 0:
            gui._click(str(nth_team_slot)+'_team_slot')
            gui.click(position['sell'])
            self.team_position[nth_team_slot - 1] = 1
        else:
            raise Exception("Invalid sell: No pet present in the slot to sell...")


    def combineInTeam(self, n1, n2):
        '''
        method to combine 2 pets that is in the team 
        combine n1 to n2
        '''
        if self.team_position[n1 - 1] == 1 or self.team_position[n2 - 1] == 1:
            raise Exception("Invalid Combine: pets in team slot is not present...")
        if 0 <= n1 <5 and 0 <= n2 <5:
            self._click(str(n1)+'_team_slot')
            self._click(str(n2)+'_team_slot')
            self.team_position[n2-1] = 0
        else:
            raise Exception("Invalid Combine: index out of range")
    
    def buyCombine(self, nth_slot , nth_team_slot):
        '''
        method to buy and combine 2 pets
        '''
        print(self.team_position[nth_team_slot - 1], nth_team_slot)
        if self.team_position[nth_team_slot - 1] == 1:
            raise Exception("Invalid buyCombine: pet in team slot not present...")    
        self._shop2team(nth_slot, nth_team_slot)

    def reorder(self, order):
        '''
        method to reorder the team
        '''
        copyOrder = order
        for i,j in enumerate(order):
            if i != j:
                self._movePet(i+1, j+1)
                del copyOrder[i]
                copyOrder.insert(j,j)
                finalOrder = self.reorder(copyOrder) # recursively solves
                return finalOrder
        return copyOrder # when all the elements are already sorted
    
    def riskyReorder(self, order):
        '''
        method to reorder the team with the assumption that there is no possible combines within the team
        '''
        pass
    
    def freezeUnfreeze(self, nth_slot):
        '''
        a method to freeze or unfreeze pets
        '''
        self._click(str(nth_slot)+'_slot')
        self._click('freeze')

    def end_turn(self, _):
        '''
        a method to end turn 
        '''
        self._click('end_turn')
    
    def roll(self):
        '''
        a method to roll
        '''
        self._click('roll')
    
    def actionDict(self):
        '''
        returns a dictionary of all the methods
        '''
        action = {}
        action['roll'] = self.roll 
        action['end_turn'] = self.end_turn
        action['reorder'] = self.reorder 
        action['buy_pet'] = self.buy
        action['buy_food'] = self.buy_food
        action['buy_food_team'] = self.buy_food
        action['sell'] = self.sell 
        action['buy_combine'] = self.buyCombine
        action['combine'] = self.combineInTeam
        return action