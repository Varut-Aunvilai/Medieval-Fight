import pygame
import random

pygame.init()
pygame.mixer.init()

#Define Class

#Warrior Class
class Warrior():
    def __init__(self):
        self.health = 300
        self.stamina = 150
        self.ultcharge = 0
        self.damage = 0
        self.block = False
    
    def Skill_1(self):  #CrushingBlow
        if self.stamina >= 30:
            self.stamina -= 30
            self.ultcharge += 20
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(30)
        else:
            return 1000

    def Skill_2(self,side): #ShieldoftheKing
        if self.stamina >= 20:
            self.stamina -= 20
        self.block = True
        return 0.1


    def Skill_3(self): #DecisiveStrike
        if self.stamina >= 80:
            self.stamina -= 80
            self.ultcharge += 20
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(50)
        else:
            return 1000

    def Skill_4(self,side): #Justice
        if(self.ultcharge == 100):
            self.ultcharge = 0
            self.stamina += 100
            if(self.stamina > 150):
                self.stamina = 150
            self.health += 50
            healnum = "+" + str(50)
            text = bigfont.render(healnum, True, (0,100,0))
            if side == 1:
                win.blit(text, (355,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(1000)
            if(self.health > 300):
                self.health = 300
            return int(120)
        else:
            return 1000

    def DamageTake(self, damage, side):
        if damage > 1:
            damage = int(damage)
            if self.block == True:
                
                self.health -= damage
                damage = "-" + str(int(damage * 0.3))
                if self.health < 0:
                    self.health = 0
                self.ultcharge += 30
                if(self.ultcharge > 100):
                    self.ultcharge = 100
                self.block = False
                damagenum = str(damage)
                text = bigfont.render(damagenum, True, (255, 0, 0))
                if side == 1:
                    win.blit(text, (335,200))
                elif side == 2:
                    win.blit(text, (755,200))
                pygame.display.update()
                pygame.time.delay(500)
                return damage
            else:
                damagenum = "-" + str(damage)
                text = bigfont.render(damagenum, True, (255, 0, 0))
                if side == 1:
                    win.blit(text, (335,200))
                elif side == 2:
                    win.blit(text, (755,200))
                pygame.display.update()
                pygame.time.delay(500)
                self.health -= damage
                if self.health < 0:
                    self.health = 0
                self.ultcharge += 20
                if(self.ultcharge > 100):
                    self.ultcharge = 100
                return text
    def Health(self):
        return self.health
    def Mana(self):
        return self.stamina
    def Skill1(self):
        return pygame.image.load('SkillIcon/Warrior/crushingblow.png')
    def Skill2(self):
        return pygame.image.load('SkillIcon/Warrior/shieldoftheking.png')
    def Skill3(self):
        return pygame.image.load('SkillIcon/Warrior/decisivestrike.png')
    def Skill4(self):
        return pygame.image.load('SkillIcon/Warrior/justice.png')
    def Regen(self,increase):
        self.stamina += increase
        if(self.stamina > 150):
            self.stamina = 150
    def Charge(self):
        return self.ultcharge
        
#Assassin Class
    
class Assassin():
    def __init__(self):
        self.health = 250
        self.stamina = 150
        self.ultcharge = 0
        self.damage = 0
        self.dodge = False
    
    def Skill_1(self): #BackStab
        if self.stamina >= 20:
            self.stamina -= 20
            self.ultcharge += 20
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(40)
        else:
            return 1000

    def Skill_2(self,side): #ShadowStep
        if self.stamina >= 40:
            self.stamina -= 40
        self.dodge = True
        return 0.1


    def Skill_3(self): #Savagery
        if self.stamina >= 60:
            self.stamina -= 60
            self.ultcharge += 30
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(60)
        else:
            return 1000

    def Skill_4(self,side): #UmbraBlades
        if(self.ultcharge == 100):
            self.ultcharge = 0
            self.stamina += 70
            if (self.stamina > 100):
                self.stamina = 100
            self.health += 60
            healnum = "+" + str(60)
            text = bigfont.render(healnum, True, (0,100,0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            if(self.health > 250):
                self.health = 250
            return int(100)
        else:
            return 1000

    def DamageTake(self, damage, side):
        if damage > 1:
            damage = int(damage)
            if self.dodge == True:
                damagenum = "-" + str(0)
                text = bigfont.render(damagenum, True, (255, 0, 0))
                if side == 1:
                    win.blit(text, (335,200))
                elif side == 2:
                    win.blit(text, (755,200))
                pygame.display.update()
                pygame.time.delay(500)
                self.ultcharge += 30
                if(self.ultcharge > 100):
                    self.ultcharge = 100
                self.dodge = False
                return int(0)
            else:
                damagenum = "-" + str(damage)
                text = bigfont.render(damagenum, True, (255, 0, 0))
                if side == 1:
                    win.blit(text, (335,200))
                elif side == 2:
                    win.blit(text, (755,200))
                pygame.display.update()
                pygame.time.delay(500)
                self.health -= damage
                if self.health < 0:
                    self.health = 0
                self.ultcharge += 20
                if(self.ultcharge > 100):
                    self.ultcharge = 100
                return damage

    def Health(self):
        return self.health
    def Mana(self):
        return self.stamina
    def Skill1(self):
        return pygame.image.load('SkillIcon/Assassin/backstab.png')
    def Skill2(self):
        return pygame.image.load('SkillIcon/Assassin/shadowstep.png')
    def Skill3(self):
        return pygame.image.load('SkillIcon/Assassin/savagery.png')
    def Skill4(self):
        return pygame.image.load('SkillIcon/Assassin/umbrablades.png')
    def Regen(self,increase):
        self.stamina += increase
        if (self.stamina > 150):
            self.stamina = 150
    def Charge(self):
        return self.ultcharge

#Wizard Class
  
class Wizard():
    def __init__(self):
        self.health = 200
        self.mana = 150
        self.ultcharge = 0
        self.damage = 0
    
    def Skill_1(self): #SpellFlux
        if self.mana >= 50:
            self.mana -= 50
            self.ultcharge += 30
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(40)
        else:
            return 1000

    def Skill_2(self,side): #MagicBlessing
        if (self.mana >= 10):
            self.mana -= 10
            self.health += 60
            healnum = "+" + str(60)
            text = bigfont.render(healnum, True, (0,100,0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            if(self.health > 200):
                self.health = 200
            self.ultcharge += 5
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return 0.1
        else:
            return 1000


    def Skill_3(self): #MeteorStrike
        if self.mana >= 80:
            self.mana -= 80
            self.ultcharge += 30
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(80)
        else:
            return 1000

    def Skill_4(self,side): #PrimordialBurst
        if(self.ultcharge == 100 and self.mana >= 50):
            self.ultcharge = 0
            self.mana -= 50
            if (self.mana < 150):
                self.mana = 150
            self.health += 80
            healnum = "+" + str(80)
            text = bigfont.render(healnum, True, (0,100,0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            if(self.health > 200):
                self.health = 200
            return int(120)
        else:
            return 1000

    def DamageTake(self, damage, side):
        if damage > 1:
            damage = int(damage)
            damagenum = "-" + str(damage)
            text = bigfont.render(damagenum, True, (255, 0, 0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            self.health -= damage
            if self.health < 0:
                self.health = 0
            self.ultcharge += 20
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return damage
    def Health(self):
        return self.health
    def Mana(self):
        return self.mana
    def Skill1(self):
        return pygame.image.load('SkillIcon/Wizard/spellflux.png')
    def Skill2(self):
        return pygame.image.load('SkillIcon/Wizard/magicbless.png')
    def Skill3(self):
        return pygame.image.load('SkillIcon/Wizard/meteorstrike.png')
    def Skill4(self):
        return pygame.image.load('SkillIcon/Wizard/primordialburst.png')
    def Regen(self,increase):
        self.mana += increase
        if (self.mana > 150):
            self.mana = 150
    def Charge(self):
        return self.ultcharge

#Witch Class

class Witch():
    def __init__(self):
        self.health = 200
        self.mana = 200
        self.ultcharge = 0
        self.damage = 0
    
    def Skill_1(self): #MysticShot
        if self.mana >= 5:
            self.mana -= 5
            self.ultcharge += 15
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(10)
        else:
            return 1000

    def Skill_2(self,side): #Drain
        if (self.mana >= 60):
            self.mana -= 60
            self.health += 80
            healnum = "+" + str(80)
            text = bigfont.render(healnum, True, (0,100,0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            if(self.health > 200):
                self.health = 200
                self.ultcharge += 15
                if(self.ultcharge > 100):
                    self.ultcharge = 100
            else:
                self.ultcharge += 10
                if(self.ultcharge > 100):
                    self.ultcharge = 100
            return int(20)
            
        else:
            return 1000


    def Skill_3(self): #Disintegrate
        if self.mana >= 80:
            self.mana -= 80
            self.ultcharge += 10
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return int(80)
        else:
            return 1000

    def Skill_4(self,side): #Requiem
        if(self.ultcharge == 100 and self.mana >= 50):
            self.ultcharge = 0
            self.mana -= 50
            if (self.mana < 200):
                self.mana = 200
            self.health += 100
            healnum = "+" + str(100)
            text = bigfont.render(healnum, True, (0,100,0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            if(self.health > 200):
                self.health = 200
            return int(150)
        else:
            return 1000

    def DamageTake(self, damage, side):
        if damage > 1:
            damage = int(damage)
            damagenum = "-" + str(damage)
            text = bigfont.render(damagenum, True, (255, 0, 0))
            if side == 1:
                win.blit(text, (335,200))
            elif side == 2:
                win.blit(text, (755,200))
            pygame.display.update()
            pygame.time.delay(500)
            self.health -= damage
            if self.health < 0:
                self.health = 0
            self.ultcharge += 20
            if(self.ultcharge > 100):
                self.ultcharge = 100
            return damage
    def Health(self):
        return self.health
    def Mana(self):
        return self.mana
    def Skill1(self):
        return pygame.image.load('SkillIcon/Witch/mysticshot.png')
    def Skill2(self):
        return pygame.image.load('SkillIcon/Witch/drain.png')
    def Skill3(self):
        return pygame.image.load('SkillIcon/Witch/disintegrate.png')
    def Skill4(self):
        return pygame.image.load('SkillIcon/Witch/requiem.png')
    def Regen(self,increase):
        self.mana += increase
        if (self.mana > 200):
            self.mana = 200
    def Charge(self):
        return self.ultcharge

       


win = pygame.display.set_mode((1200,800))

pygame.display.set_caption("Medival Fight")

font = pygame.font.SysFont("comicsansms", 24)
bigfont = pygame.font.SysFont("comicsansms", 50)

#Picture

WarriorStandP1 = [pygame.image.load('Charactor/Warrior/P1/WarriorStand.png')]
WarriorShieldHitP1 = [pygame.image.load('Charactor/Warrior/P1/WarriorShieldHit1.png'),
                      pygame.image.load('Charactor/Warrior/P1/WarriorShieldHit2.png')]
WarriorDefenceP1 = [pygame.image.load('Charactor/Warrior/P1/WarriorShieldHit1.png')]
WarriorSlashP1 = [pygame.image.load('Charactor/Warrior/P1/WarriorSlash1.png'),
                  pygame.image.load('Charactor/Warrior/P1/WarriorSlash2.png'),
                  pygame.image.load('Charactor/Warrior/P1/WarriorSlash1.png'),
                  pygame.image.load('Charactor/Warrior/P1/WarriorSlash2.png')]
WarriorUltP1 = [pygame.image.load('Charactor/Warrior/P1/WarriorUlt1.png'),
                pygame.image.load('Charactor/Warrior/P1/WarriorUlt2.png')]

WarriorStandP2 = [pygame.image.load('Charactor/Warrior/P2/WarriorStand.png')]
WarriorShieldHitP2 = [pygame.image.load('Charactor/Warrior/P2/WarriorShieldHit1.png'),
                      pygame.image.load('Charactor/Warrior/P2/WarriorShieldHit2.png')]
WarriorDefenceP2 = [pygame.image.load('Charactor/Warrior/P2/WarriorShieldHit1.png')]
WarriorSlashP2 = [pygame.image.load('Charactor/Warrior/P2/WarriorSlash1.png'),
                  pygame.image.load('Charactor/Warrior/P2/WarriorSlash2.png'),
                  pygame.image.load('Charactor/Warrior/P2/WarriorSlash1.png'),
                  pygame.image.load('Charactor/Warrior/P2/WarriorSlash2.png')]
WarriorUltP2 = [pygame.image.load('Charactor/Warrior/P2/WarriorUlt1.png'),
                pygame.image.load('Charactor/Warrior/P2/WarriorUlt2.png')]

AssassinStandP1 = [pygame.image.load('Charactor/Assassin/P1/AssassinStand.png')]
AssassinStabP1 = [pygame.image.load('Charactor/Assassin/P2/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab2.png')]
AssassinStab2P1 = [pygame.image.load('Charactor/Assassin/P1/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab2.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab2.png')]
AssassinShadowP1 = [pygame.image.load('Charactor/Assassin/P1/AssassinUlt1.png'),
                    pygame.image.load('Charactor/Assassin/P1/AssassinUlt2.png'),
                    pygame.image.load('Charactor/Assassin/P1/AssassinUlt2.png')]
AssassinUltP1 = [pygame.image.load('Charactor/Assassin/P1/AssassinUlt1.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt2.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt3.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt4.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt5.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt6.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt7.png'),
                 pygame.image.load('Charactor/Assassin/P1/AssassinUlt8.png')]

AssassinStandP2 = [pygame.image.load('Charactor/Assassin/P2/AssassinStand.png')]
AssassinStabP2 = [pygame.image.load('Charactor/Assassin/P1/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P1/AssassinStab2.png')]
AssassinStab2P2 = [pygame.image.load('Charactor/Assassin/P2/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab2.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab0.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab1.png'),
                  pygame.image.load('Charactor/Assassin/P2/AssassinStab2.png'),]
AssassinShadowP2 = [pygame.image.load('Charactor/Assassin/P2/AssassinUlt1.png'),
                    pygame.image.load('Charactor/Assassin/P2/AssassinUlt2.png'),
                    pygame.image.load('Charactor/Assassin/P2/AssassinUlt2.png')]
AssassinUltP2 = [pygame.image.load('Charactor/Assassin/P2/AssassinUlt1.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt2.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt3.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt4.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt5.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt6.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt7.png'),
                 pygame.image.load('Charactor/Assassin/P2/AssassinUlt8.png')]

WizardStandP1 = [pygame.image.load('Charactor/Wizard/P1/WizardStand.png')]
WizardAttackP1 = [pygame.image.load('Charactor/Wizard/P1/WizardAttack1.png'),
                  pygame.image.load('Charactor/Wizard/P1/WizardAttack2.png')]
WizardUltP1 = [pygame.image.load('Charactor/Wizard/P1/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt2.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt2.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt2.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P1/WizardUlt2.png')]

WizardStandP2 = [pygame.image.load('Charactor/Wizard/P2/WizardStand.png')]
WizardAttackP2 = [pygame.image.load('Charactor/Wizard/P2/WizardAttack1.png'),
                  pygame.image.load('Charactor/Wizard/P2/WizardAttack2.png')]
WizardUltP2 = [pygame.image.load('Charactor/Wizard/P2/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt2.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt2.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt2.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt1.png'),
               pygame.image.load('Charactor/Wizard/P2/WizardUlt2.png')]

WitchStandP1 = [pygame.image.load('Charactor/Witch/P1/WitchStand0.png'),
                pygame.image.load('Charactor/Witch/P1/WitchStand1.png'),
                pygame.image.load('Charactor/Witch/P1/WitchStand2.png'),
                pygame.image.load('Charactor/Witch/P1/WitchStand3.png')]
WitchAttackP1 = [pygame.image.load('Charactor/Witch/P1/WitchAttack1.png'),
                 pygame.image.load('Charactor/Witch/P1/WitchAttack2.png'),
                 pygame.image.load('Charactor/Witch/P1/WitchAttack3.png')]
WitchUltP1 = [pygame.image.load('Charactor/Witch/P1/WitchUlt0.png'),
              pygame.image.load('Charactor/Witch/P1/WitchUlt1.png'),
              pygame.image.load('Charactor/Witch/P1/WitchUlt2.png'),
              pygame.image.load('Charactor/Witch/P1/WitchUlt2.png'),]

                 
WitchStandP2 = [pygame.image.load('Charactor/Witch/P2/WitchStand0.png'),
                pygame.image.load('Charactor/Witch/P2/WitchStand1.png'),
                pygame.image.load('Charactor/Witch/P2/WitchStand2.png'),
                pygame.image.load('Charactor/Witch/P2/WitchStand3.png')]
WitchAttackP2 = [pygame.image.load('Charactor/Witch/P2/WitchAttack1.png'),
                 pygame.image.load('Charactor/Witch/P2/WitchAttack2.png'),
                 pygame.image.load('Charactor/Witch/P2/WitchAttack3.png')]
WitchUltP2 = [pygame.image.load('Charactor/Witch/P2/WitchUlt0.png'),
              pygame.image.load('Charactor/Witch/P2/WitchUlt1.png'),
              pygame.image.load('Charactor/Witch/P2/WitchUlt2.png'),
              pygame.image.load('Charactor/Witch/P2/WitchUlt2.png'),]

WarriorSkillDes = [pygame.image.load('Text/Description/DescriptionwithSchroll/War1.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/War2.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/War3.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/War4.png')]
AssassinSkillDes = [pygame.image.load('Text/Description/DescriptionwithSchroll/Assassin1.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Assassin2.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Assassin3.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Assassin4.png')]
WizardSkillDes = [pygame.image.load('Text/Description/DescriptionwithSchroll/Wizard1.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Wizard2.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Wizard3.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Wizard4.png')]
WitchSkillDes = [pygame.image.load('Text/Description/DescriptionwithSchroll/Witch1.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Witch2.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Witch3.png'),
                   pygame.image.load('Text/Description/DescriptionwithSchroll/Witch4.png')]
SkipSkillDes = pygame.image.load('Text/Description/DescriptionwithSchroll/Skip.png')



bg = pygame.image.load('BG/oru8fn8iq39zS6Kcr4f-o.jpg')
BgList = [pygame.image.load('BG/BG1.jpg'),
          pygame.image.load('BG/BG2.jpg'),
          pygame.image.load('BG/BG3.jpg'),
          pygame.image.load('BG/BG4.jpg'),
          pygame.image.load('BG/BG5.jpg')]
scroll = pygame.image.load('scroll.png')
scrollskill = pygame.image.load('scrollforskill1.png')
clock = pygame.time.Clock()
warrioricon = pygame.image.load('chaIcon/Warrioricon.png')
assassinicon = pygame.image.load('chaIcon/Assassinicon.png')
wizardicon = pygame.image.load('chaIcon/Wizardicon.png')
witchicon = pygame.image.load('chaIcon/Witchicon.png')
P1square = pygame.image.load('chaIcon/P1icon.png')
P2square = pygame.image.load('chaIcon/P2icon.png')
P1skillsquare = pygame.image.load('SkillIcon/P1skillicon.png')
P2skillsquare = pygame.image.load('SkillIcon/P2skillicon.png')
Skip = pygame.image.load('SkillIcon/skip.png')

Titlenametext = pygame.image.load('Text/MedivalFight.png')
PressStarttext = [pygame.image.load('Text/Start/PressStart.png'),
                  pygame.image.load('Text/Start/PressStart1.png'),
                  pygame.image.load('Text/Start/PressStart2.png'),
                  pygame.image.load('Text/Start/PressStart3.png'),
                  pygame.image.load('Text/Start/PressStart4.png')]
P1text = pygame.image.load('Text/P1.png')
P2text = pygame.image.load('Text/P2.png')
descriptionchascroll = pygame.image.load('scrollforname.png')
namewarrior = pygame.image.load('Text/ChaName/NamewithScorll/Warrior.png')
nameassassin = pygame.image.load('Text/ChaName/NamewithScorll/Assassin.png')
namewizard = pygame.image.load('Text/ChaName/NamewithScorll/Wizard.png')
namewitch = pygame.image.load('Text/ChaName/NamewithScorll/Witch.png')
Turntext = [pygame.image.load('Text/Turn/P1Turn.png'),
            pygame.image.load('Text/Turn/P2Turn.png')]

P1Win = [pygame.image.load('Text/End/P1/P1Win1.png'),
         pygame.image.load('Text/End/P1/P1Win2.png'),
         pygame.image.load('Text/End/P1/P1Win3.png'),
         pygame.image.load('Text/End/P1/P1Win4.png'),
         pygame.image.load('Text/End/P1/P1Win5.png')]
P2Win = [pygame.image.load('Text/End/P2/P2Win1.png'),
         pygame.image.load('Text/End/P2/P2Win2.png'),
         pygame.image.load('Text/End/P2/P2Win3.png'),
         pygame.image.load('Text/End/P2/P2Win4.png'),
         pygame.image.load('Text/End/P2/P2Win5.png')]

Continuetext = pygame.image.load('Text/End/continue.png')

WarriorSound1 = pygame.mixer.Sound('Sound/1/Gar.ogx')
WarriorSound2 = pygame.mixer.Sound('Sound/2/Gar.ogx')
WarriorSound3 = pygame.mixer.Sound('Sound/3/Gar.ogx')
WarriorSound4 = pygame.mixer.Sound('Sound/ULT/Gar.ogx')

AssassinSound1 = pygame.mixer.Sound('Sound/1/Noc.ogx')
AssassinSound2 = pygame.mixer.Sound('Sound/2/Noc.ogx')
AssassinSound3 = pygame.mixer.Sound('Sound/3/Noc.ogx')
AssassinSound4 = pygame.mixer.Sound('Sound/ULT/Noc.ogx')

WizardSound1 = pygame.mixer.Sound('Sound/1/Vei.ogx')
WizardSound2 = pygame.mixer.Sound('Sound/2/Vei.ogx')
WizardSound3 = pygame.mixer.Sound('Sound/3/Vei.ogx')
WizardSound4 = pygame.mixer.Sound('Sound/ULT/Vei.ogx')

WitchSound1 = pygame.mixer.Sound('Sound/1/Siv.oga')
WitchSound2 = pygame.mixer.Sound('Sound/2/Siv.ogx')
WitchSound3 = pygame.mixer.Sound('Sound/3/Siv.ogx')
WitchSound4 = pygame.mixer.Sound('Sound/ULT/Siv.ogx')


#global variable

skillCount = 0
skillUltCount = 0
standCount = 0
standCount2 = 0
StartCount = 0
endCount = 0

randBG = random.randint(0,4)

#function start

def redrawStartWindow(randBG):
    global StartCount
    
    win.blit(BgList[randBG], (0,0))
    win.blit(Titlenametext, (200,200))
    if StartCount +1 > 10:
        StartCount = 0
    win.blit(PressStarttext[StartCount//2], (400,700))
    StartCount += 1
    pygame.display.update()

#function choose charactor

def redrawChooseWindow(randBG):


    win.blit(BgList[randBG], (0,0))

    win.blit(P1text, (230, 50))
    win.blit(scroll, (50,150))
    win.blit(P1square, (p1x,p1y))


    win.blit(warrioricon, (180, 320))
    win.blit(assassinicon, (320, 320))
    win.blit(wizardicon, (180, 470))
    win.blit(witchicon, (320, 470))

    #player 1 charactor name

    if WarriorNameP1:
        win.blit(namewarrior, (60, 550))
    if AssassinNameP1:
        win.blit(nameassassin, (60, 550))
    if WizardNameP1:
        win.blit(namewizard, (60, 550))
    if WitchNameP1:
        win.blit(namewitch, (60, 550))
    
    
    
        

    
    win.blit(P2text, (830, 50))
    win.blit(scroll, (650,150))

    win.blit(P2square, (p2x,p2y))

    #player 1 charactor name

    if WarriorNameP2:
        win.blit(namewarrior, (660, 550))
    if AssassinNameP2:
        win.blit(nameassassin, (660, 550))
    if WizardNameP2:
        win.blit(namewizard, (660, 550))
    if WitchNameP2:
        win.blit(namewitch, (660, 550))

    
    win.blit(warrioricon, (780, 320))
    win.blit(assassinicon, (920, 320))
    win.blit(wizardicon, (780, 470))
    win.blit(witchicon, (920, 470))

    
    pygame.display.update()

#function play

def redrawGamePlay(P1Char,P2Char,randBG):
    global standCount
    global skillCount
    global skillUltCount
    global standCount2
    
    win.blit(BgList[randBG], (0,0))

    #turn

    if TurnP1:
        win.blit(Turntext[0], (460, 50))
    if TurnP2:
        win.blit(Turntext[1], (460, 50))

    #player 1 charactor movement

    if P1Stand:
        if P1Char == 1:
            win.blit(WarriorStandP1[standCount2], (300,100))
        elif P1Char == 2:
            win.blit(AssassinStandP1[standCount2], (300,300))
        elif P1Char == 3:
            win.blit(WizardStandP1[standCount2], (325,250))
        elif P1Char == 4:
            if standCount +1 > 12:
                standCount = 0
            win.blit(WitchStandP1[standCount//3], (335,300))
            standCount += 1
    if P1Skill1:
        if P1Char == 1:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WarriorShieldHitP1[skillCount//6], (600,100))
            skillCount += 1
        elif P1Char == 2:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(AssassinStabP1[skillCount//2], (770,300))
            skillCount += 1
            pygame.time.delay(50)
        elif P1Char == 3:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WizardAttackP1[skillCount//6], (325,250))
            skillCount += 1
        elif P1Char == 4:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WitchAttackP1[skillCount//4], (335,300))
            skillCount += 1
    if P1Skill2:
        if P1Char == 1:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WarriorShieldHitP1[skillCount//12], (300,100))
            skillCount += 1
        elif P1Char == 2:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(AssassinShadowP1[skillCount//4], (300,300))
            skillCount += 1
        elif P1Char == 3:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WizardAttackP1[skillCount//6], (325,250))
            skillCount += 1
        elif P1Char == 4:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WitchAttackP1[skillCount//4], (335,300))
            skillCount += 1
    if P1Skill3:
        if P1Char == 1:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WarriorSlashP1[skillCount//3], (550,100))
            skillCount += 1
        elif P1Char == 2:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(AssassinStab2P1[skillCount//2], (600,300))
            skillCount += 1
        elif P1Char == 3:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WizardAttackP1[skillCount//6], (325,250))
            skillCount += 1
        elif P1Char == 4:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WitchAttackP1[skillCount//4], (335,300))
            skillCount += 1
    if P1Skill4:
        if P1Char == 1:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(WarriorUltP1[skillUltCount//12], (300,100))
            skillUltCount += 1
        elif P1Char == 2:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(AssassinUltP1[skillUltCount//3], (500,300))
            skillUltCount += 1
        elif P1Char == 3:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(WizardUltP1[skillUltCount//3], (325,250))
            skillUltCount += 1
        elif P1Char == 4:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(WitchUltP1[skillUltCount//8], (335,300))
            skillUltCount += 1

    #player 1 hp, mp, ult
    
    pygame.draw.rect(win, (0, 0, 0), (20, 20,((P1Bhp*1.5) + 10), 40))
    pygame.draw.rect(win, (255, 0, 0), (25, 25,(P1hp*1.5), 30))
    pygame.draw.rect(win, (0, 0, 0), (20, 55,((P1Bmp*1.5) + 10), 30))
    pygame.draw.rect(win, (102, 167, 255), (25, 60,(P1mp*1.5), 20))
    pygame.draw.rect(win, (0, 0, 0), (20, 80,((100*1.5) + 10), 30))
    pygame.draw.rect(win, (0, 255, 0), (25, 85,(P1Charge*1.5), 20))

    #player 1 skill description

    if TurnP1:
        if(P1Char == 1):
            if Skill1Des:
                win.blit(WarriorSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(WarriorSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(WarriorSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(WarriorSkillDes[3], (235, 520))
        if(P1Char == 2):
            if Skill1Des:
                win.blit(AssassinSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(AssassinSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(AssassinSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(AssassinSkillDes[3], (235, 520))
        if(P1Char == 3):
            if Skill1Des:
                win.blit(WizardSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(WizardSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(WizardSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(WizardSkillDes[3], (235, 520))
        if(P1Char == 4):
            if Skill1Des:
                win.blit(WitchSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(WitchSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(WitchSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(WitchSkillDes[3], (235, 520))

    #player 2 skill description
    
    if TurnP2:
        if(P2Char == 1):
            if Skill1Des:
                win.blit(WarriorSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(WarriorSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(WarriorSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(WarriorSkillDes[3], (235, 520))
        if(P2Char == 2):
            if Skill1Des:
                win.blit(AssassinSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(AssassinSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(AssassinSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(AssassinSkillDes[3], (235, 520))
        if(P2Char == 3):
            if Skill1Des:
                win.blit(WizardSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(WizardSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(WizardSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(WizardSkillDes[3], (235, 520))
        if(P2Char == 4):
            if Skill1Des:
                win.blit(WitchSkillDes[0], (235, 520))
            if Skill2Des:
                win.blit(WitchSkillDes[1], (235, 520))
            if Skill3Des:
                win.blit(WitchSkillDes[2], (235, 520))
            if Skill4Des:
                win.blit(WitchSkillDes[3], (235, 520))
    if SkipDes:
                win.blit(SkipSkillDes, (235, 520))
        

    #player 2 charactor movement

    if P2Stand:
        if P2Char == 1:
            win.blit(WarriorStandP2[standCount2], (650,100))
        elif P2Char == 2:
            win.blit(AssassinStandP2[standCount2], (645,300))
        elif P2Char == 3:
            win.blit(WizardStandP2[standCount2], (650,250))
        elif P2Char == 4:
            if standCount +1 > 12:
                standCount = 0
            win.blit(WitchStandP2[standCount//3], (650,300))
            standCount += 1
    if P2Skill1:
        if P2Char == 1:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WarriorShieldHitP2[skillCount//6], (350,100))
            skillCount += 1
        elif P2Char == 2:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(AssassinStabP2[skillCount//2], (175,300))
            skillCount += 1
            pygame.time.delay(100)
        elif P2Char == 3:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WizardAttackP2[skillCount//6], (650,250))
            skillCount += 1
        elif P2Char == 4:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WitchAttackP2[skillCount//4], (650,300))
            skillCount += 1
    if P2Skill2:
        if P2Char == 1:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WarriorShieldHitP2[skillCount//12], (650,100))
            skillCount += 1
        elif P2Char == 2:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(AssassinShadowP2[skillCount//4], (645,300))
            skillCount += 1
        elif P2Char == 3:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WizardAttackP2[skillCount//6], (650,250))
            skillCount += 1
        elif P2Char == 4:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WitchAttackP2[skillCount//4], (650,300))
            skillCount += 1
    if P2Skill3:
        if P2Char == 1:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WarriorSlashP2[skillCount//3], (400,100))
            skillCount += 1
        elif P2Char == 2:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(AssassinStab2P2[skillCount//2], (350,300))
            skillCount += 1
        elif P2Char == 3:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WizardAttackP2[skillCount//6], (650,250))
            skillCount += 1
        elif P2Char == 4:
            if skillCount +1 > 12:
                skillCount = 0
            win.blit(WitchAttackP2[skillCount//4], (650,300))
            skillCount += 1
    if P2Skill4:
        if P2Char == 1:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(WarriorUltP2[skillUltCount//12], (650,100))
            skillUltCount += 1
        elif P2Char == 2:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(AssassinUltP2[skillUltCount//3], (420,300))
            skillUltCount += 1
        elif P2Char == 3:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(WizardUltP2[skillUltCount//3], (650,250))
            skillUltCount += 1
        elif P2Char == 4:
            if skillUltCount +1 > 24:
                skillUltCount = 0
            win.blit(WitchUltP2[skillUltCount//8], (650,300))
            skillUltCount += 1

    #player 2 hp, mp, ult
                
    pygame.draw.rect(win, (0, 0, 0), (1180, 20, ((P2Bhp*1.5) + 10)*(-1), 40))
    pygame.draw.rect(win, (255, 0, 0), (1175, 25, (P2hp*1.5)*(-1), 30))
    pygame.draw.rect(win, (0, 0, 0), (1180, 55,((P2Bmp*1.5) + 10)*(-1), 30))
    pygame.draw.rect(win, (102, 167, 255), (1175, 60,(P2mp*1.5)*(-1), 20))
    pygame.draw.rect(win, (0, 0, 0), (1180, 80,((100*1.5) + 10)*(-1), 30))
    pygame.draw.rect(win, (0, 255, 0), (1175, 85,(P2Charge*1.5)*(-1), 20))

    #skill tab

    win.blit(scrollskill, (20, 150))
    win.blit(scrollskill, (930, 150))

    
    win.blit(P1skillsquare, (p1skx, p1sky))
    win.blit(P1skill1, (120, 230))
    win.blit(P1skill2, (120, 320))
    win.blit(P1skill3, (120, 410))
    win.blit(P1skill4, (120, 500))
    win.blit(Skip, (120, 590))
    


    win.blit(P2skillsquare, (p2skx, p2sky))
    win.blit(P2skill1, (1020, 230))
    win.blit(P2skill2, (1020, 320))
    win.blit(P2skill3, (1020, 410))
    win.blit(P2skill4, (1020, 500))
    win.blit(Skip, (1020, 590))

    text = font.render(P1hpnum, True, (255, 255, 255))
    win.blit(text, (40,20))
    text = font.render(P2hpnum, True, (255, 255, 255))
    win.blit(text, (1055,20))
    text = font.render(P1mpnum, True, (255, 255, 255))
    win.blit(text, (40,52))
    text = font.render(P2mpnum, True, (255, 255, 255))
    win.blit(text, (1055,52))
    text = font.render(P1chargenum, True, (255, 255, 255))
    win.blit(text, (40,80))
    text = font.render(P2chargenum, True, (255, 255, 255))
    win.blit(text, (1055,80))




    pygame.display.update()

#end

def redrawEndWindow(randBG):
    global endCount
    
    win.blit(BgList[randBG], (0,0))

    #player 1 or player 2 win

    if P1Dead:
        if endCount +1 > 10:
            endCount = 0
        win.blit(P2Win[endCount//2], (350,100))
        endCount += 1
    if P2Dead:
        if endCount +1 > 10:
            endCount = 0
        win.blit(P1Win[endCount//2], (350,100))
        endCount += 1

    win.blit(Continuetext, (350, 500))



        
    pygame.display.update()
    
run = True
start = True

#start the game

while start:
    redrawStartWindow(randBG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        start = False
        pygame.time.delay(250)


#loop if play again

while run:

    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    p1x = 170
    p1y = 310
    p2x = 770
    p2y = 310

    p1skx = 110
    p1sky = 220
    p2skx = 1010
    p2sky = 220


    P1Char = 0
    P2Char = 0
    WarriorNameP1 = False
    AssassinNameP1 = False
    WizardNameP1 = False
    WitchNameP1 = False

    WarriorNameP2 = False
    AssassinNameP2 = False
    WizardNameP2 = False
    WitchNameP2 = False

    chosep1 = True
    chosep2 = True

    #choosing charactor

    while (chosep1 or chosep2):
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()


        if(chosep1 == True):
            if keys[pygame.K_w] and p1y == 460:
                p1y = 310
            elif keys[pygame.K_a] and p1x == 310:
                p1x = 170
            elif keys[pygame.K_s] and p1y == 310:
                p1y = 460
            elif keys[pygame.K_d] and p1x == 170:
                p1x = 310
            elif keys[pygame.K_SPACE]:
                if(p1x == 170 and p1y == 310):
                    P1 = Warrior()
                    P1Char = 1
                    chosep1 = False
                elif(p1x == 310 and p1y == 310):
                    P1 = Assassin()
                    P1Char = 2
                    chosep1 = False
                elif(p1x == 170 and p1y == 460):
                    P1 = Wizard()
                    P1Char = 3
                    chosep1 = False
                elif(p1x == 310 and p1y == 460):
                    P1 = Witch()
                    P1Char = 4
                    chosep1 = False
                pygame.time.delay(70)

                
            if (p1x == 170 and p1y == 310):
                WarriorNameP1 = True
                AssassinNameP1 = False
                WizardNameP1 = False
                WitchNameP1 = False
            elif (p1x == 310 and p1y == 310):
                WarriorNameP1 = False
                AssassinNameP1 = True
                WizardNameP1 = False
                WitchNameP1 = False
            elif (p1x == 170 and p1y == 460):
                WarriorNameP1 = False
                AssassinNameP1 = False
                WizardNameP1 = True
                WitchNameP1 = False
            elif (p1x == 310 and p1y == 460):
                WarriorNameP1 = False
                AssassinNameP1 = False
                WizardNameP1 = False
                WitchNameP1 = True
                
            redrawChooseWindow(randBG)


        if(chosep2 == True):
        
            if keys[pygame.K_UP] and p2y == 460:
                p2y = 310
            elif keys[pygame.K_LEFT] and p2x == 910:
                p2x = 770
            elif keys[pygame.K_DOWN] and p2y == 310:
                p2y = 460
            elif keys[pygame.K_RIGHT] and p2x == 770:
                p2x = 910
            elif keys[pygame.K_KP_ENTER]:
                if(p2x == 770 and p2y == 310):
                    P2 = Warrior()
                    P2Char = 1
                    chosep2 = False
                elif(p2x == 910 and p2y == 310):
                    P2 = Assassin()
                    P2Char = 2
                    chosep2 = False
                elif(p2x == 770 and p2y == 460):
                    P2 = Wizard()
                    P2Char = 3
                    chosep2 = False
                elif(p2x == 910 and p2y == 460):
                    P2 = Witch()
                    P2Char = 4
                    chosep2 = False
                pygame.time.delay(70)

            if (p2x == 770 and p2y == 310):
                WarriorNameP2 = True
                AssassinNameP2 = False
                WizardNameP2 = False
                WitchNameP2 = False
            elif (p2x == 910 and p2y == 310):
                WarriorNameP2 = False
                AssassinNameP2 = True
                WizardNameP2 = False
                WitchNameP2 = False
            elif (p2x == 770 and p2y == 460):
                WarriorNameP2 = False
                AssassinNameP2 = False
                WizardNameP2 = True
                WitchNameP2 = False
            elif (p2x == 910 and p2y == 460):
                WarriorNameP2 = False
                AssassinNameP2 = False
                WizardNameP2 = False
                WitchNameP2 = True
            redrawChooseWindow(randBG)
            
    P1Bhp = P1.Health()
    P2Bhp = P2.Health()
    P1Bmp = P1.Mana()
    P2Bmp = P2.Mana()


    P1hp = P1.Health()
    P2hp = P2.Health()
    P1mp = P1.Mana()
    P2mp = P2.Mana()
    P1skill1 = P1.Skill1()
    P1skill2 = P1.Skill2()
    P1skill3 = P1.Skill3()
    P1skill4 = P1.Skill4()
    P2skill1 = P2.Skill1()
    P2skill2 = P2.Skill2()
    P2skill3 = P2.Skill3()
    P2skill4 = P2.Skill4()
    P1Charge = P1.Charge()
    P2Charge = P2.Charge()


    P1hpnum = str(int(P1hp)) + "/" + str(P1Bhp)
    P2hpnum = str(int(P2hp)) + "/" + str(P2Bhp)
    P1mpnum = str(int(P1mp)) + "/" + str(P1Bmp)
    P2mpnum = str(int(P2mp)) + "/" + str(P2Bmp)
    P1chargenum = str(int(P1Charge)) + "/" + str(100)
    P2chargenum = str(int(P2Charge)) + "/" + str(100)

    P1Skill1 = False
    P1Skill2 = False
    P1Skill3 = False
    P1Skill4 = False
    P1Stand = True

    P2Skill1 = False
    P2Skill2 = False
    P2Skill3 = False
    P2Skill4 = False
    P2Stand = True

    Skill1Des = False
    Skill2Des = False
    Skill3Des = False
    Skill4Des = False
    SkipDes = False

    TurnP1 = False
    TurnP2 = False
    turn = 1
    P1Dead = False
    P2Dead = False

    #playing

    while (P1hp != 0 and P2hp != 0):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        
        redrawGamePlay(P1Char,P2Char,randBG)

        
        if (turn%2 == 1):
            TurnP1 = True
            TurnP2 = False
        elif (turn%2 == 0):
            TurnP1 = False
            TurnP2 = True
            
            
        
        #player 1 skill
        
        if(TurnP1 == True):
            if keys[pygame.K_w] and p1sky > 220:
                p1sky -= 90
                pygame.time.delay(70)
            elif keys[pygame.K_s] and p1sky < 580:
                p1sky += 90
                pygame.time.delay(70)
            
            elif keys[pygame.K_SPACE]:
                if(p1sky == 220):
                    damage = P1.Skill_1()
                    if damage<1000:
                        P1Skill1 = True
                        P1Skill2 = False
                        P1Skill3 = False
                        P1Skill4 = False
                        P1Stand = False
                        if P1Char == 1:
                            WarriorSound1.play()
                            pygame.time.delay(500)
                        elif P1Char == 2:
                            AssassinSound1.play()
                        elif P1Char == 3:
                            WizardSound1.play()
                        elif P1Char == 4:
                            WitchSound1.play()
                            pygame.time.delay(750)
                        for i in range(12):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P2.DamageTake(damage, 2)
                        P2.Regen(20)
                        pygame.time.delay(750)
                        turn += 1
                        P1Stand = True
                        P1Skill1 = False
                    else:
                        turn += 0
                elif(p1sky == 310):
                    damage = P1.Skill_2(1)
                    if damage<1000:
                        P1Skill1 = False
                        P1Skill2 = True
                        P1Skill3 = False
                        P1Skill4 = False
                        P1Stand = False
                        if P1Char == 1:
                            WarriorSound2.play()
                        elif P1Char == 2:
                            AssassinSound2.play()
                        elif P1Char == 3:
                            WizardSound2.play()
                        elif P1Char == 4:
                            WitchSound2.play()
                        for i in range(12):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P2.DamageTake(damage, 2)
                        P2.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P1Stand = True
                        P1Skill2 = False
                    else:
                        turn += 0
                elif(p1sky == 400):
                    damage = P1.Skill_3()
                    if damage<1000:
                        P1Skill1 = False
                        P1Skill2 = False
                        P1Skill3 = True
                        P1Skill4 = False
                        P1Stand = False
                        if P1Char == 1:
                            WarriorSound3.play()
                        elif P1Char == 2:
                            AssassinSound3.play()
                        elif P1Char == 3:
                            WizardSound3.play()
                        elif P1Char == 4:
                            WitchSound3.play()
                        for i in range(12):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P2.DamageTake(damage, 2)
                        P2.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P1Stand = True
                        P1Skill3 = False
                    else:
                        turn += 0
                elif(p1sky == 490):
                    damage = P1.Skill_4(1)
                    if damage<1000:
                        P1Skill1 = False
                        P1Skill2 = False
                        P1Skill3 = False
                        P1Skill4 = True
                        P1Stand = False
                        if P1Char == 1:
                            WarriorSound4.play()
                        elif P1Char == 2:
                            AssassinSound4.play()
                        elif P1Char == 3:
                            WizardSound4.play()
                        elif P1Char == 4:
                            WitchSound4.play()
                        for i in range(24):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P2.DamageTake(damage, 2)
                        P2.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P1Stand = True
                        P1Skill4 = False
                    else:
                        turn += 0
                elif(p1sky == 580):
                    P1.Regen(20)
                    turn += 1

            #player 1 skill description
                    
            if (TurnP1 and p1sky == 220):
                Skill1Des = True
                Skill2Des = False
                Skill3Des = False
                Skill4Des = False
                SkipDes = False
            elif (TurnP1 and p1sky == 310):
                Skill1Des = False
                Skill2Des = True
                Skill3Des = False
                Skill4Des = False
                SkipDes = False
            elif (TurnP1 and p1sky == 400):
                Skill1Des = False
                Skill2Des = False
                Skill3Des = True
                Skill4Des = False
                SkipDes = False
            elif (TurnP1 and p1sky == 490):
                Skill1Des = False
                Skill2Des = False
                Skill3Des = False
                Skill4Des = True
                SkipDes = False
            elif (TurnP1 and p1sky == 580):
                Skill1Des = False
                Skill2Des = False
                Skill3Des = False
                Skill4Des = False
                SkipDes = True

        #player 2 skill
                
        if(TurnP2 == True):
        
            if keys[pygame.K_UP] and p2sky > 220:
                p2sky -= 90
                pygame.time.delay(70)
            elif keys[pygame.K_DOWN] and p2sky < 580:
                p2sky += 90
                pygame.time.delay(70)

            elif keys[pygame.K_KP_ENTER]:
                if(p2sky == 220):
                    damage = P2.Skill_1()
                    if damage<1000:
                        P2Skill1 = True
                        P2Skill2 = False
                        P2Skill3 = False
                        P2Skill4 = False
                        P2Stand = False
                        if P2Char == 1:
                            WarriorSound1.play()
                        elif P2Char == 2:
                            AssassinSound1.play()
                        elif P2Char == 3:
                            WizardSound1.play()
                        elif P2Char == 4:
                            WitchSound1.play()
                        for i in range(12):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P1.DamageTake(damage, 1)
                        P1.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P2Stand = True
                        P2Skill1 = False
                    else:
                        turn += 0
                elif(p2sky == 310):
                    damage = P2.Skill_2(2)
                    if damage<1000:
                        P2Skill1 = False
                        P2Skill2 = True
                        P2Skill3 = False
                        P2Skill4 = False
                        P2Stand = False
                        if P2Char == 1:
                            WarriorSound2.play()
                        elif P2Char == 2:
                            AssassinSound2.play()
                        elif P2Char == 3:
                            WizardSound2.play()
                        elif P2Char == 4:
                            WitchSound2.play()
                        for i in range(12):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P1.DamageTake(damage, 1)
                        P1.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P2Stand = True
                        P2Skill2 = False
                    else:
                        turn += 0
                elif(p2sky == 400):
                    damage = P2.Skill_3()
                    if damage<1000:
                        P2Skill1 = False
                        P2Skill2 = False
                        P2Skill3 = True
                        P2Skill4 = False
                        P2Stand = False
                        if P2Char == 1:
                            WarriorSound3.play()
                        elif P2Char == 2:
                            AssassinSound3.play()
                        elif P2Char == 3:
                            WizardSound3.play()
                        elif P2Char == 4:
                            WitchSound3.play()
                        for i in range(12):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P1.DamageTake(damage, 1)
                        P1.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P2Stand = True
                        P2Skill3 = False
                    else:
                        turn += 0
                elif(p2sky == 490):
                    damage = P2.Skill_4(2)
                    if damage<1000:
                        P2Skill1 = False
                        P2Skill2 = False
                        P2Skill3 = False
                        P2Skill4 = True
                        P2Stand = False
                        if P2Char == 1:
                            WarriorSound4.play()
                        elif P2Char == 2:
                            AssassinSound4.play()
                        elif P2Char == 3:
                            WizardSound4.play()
                        elif P2Char == 4:
                            WitchSound4.play()
                        for i in range(24):
                            redrawGamePlay(P1Char,P2Char,randBG)
                        P1.DamageTake(damage, 1)
                        P1.Regen(20)
                        pygame.time.delay(1000)
                        turn += 1
                        P2Stand = True
                        P2Skill4 = False
                    else:
                        turn += 0
                elif(p2sky == 580):
                    P2.Regen(20)
                    turn += 1

            #player 2 skill description
                    
            if (TurnP2 and p2sky == 220):
                Skill1Des = True
                Skill2Des = False
                Skill3Des = False
                Skill4Des = False
                SkipDes = False
            elif (TurnP2 and p2sky == 310):
                Skill1Des = False
                Skill2Des = True
                Skill3Des = False
                Skill4Des = False
                SkipDes = False
            elif (TurnP2 and p2sky == 400):
                Skill1Des = False
                Skill2Des = False
                Skill3Des = True
                Skill4Des = False
                SkipDes = False
            elif (TurnP2 and p2sky == 490):
                Skill1Des = False
                Skill2Des = False
                Skill3Des = False
                Skill4Des = True
                SkipDes = False
            elif (TurnP2 and p2sky == 580):
                Skill1Des = False
                Skill2Des = False
                Skill3Des = False
                Skill4Des = False
                SkipDes = True

        P1hp = P1.Health()
        P2hp = P2.Health()
        P1mp = P1.Mana()
        P2mp = P2.Mana()
        P1Charge = P1.Charge()
        P2Charge = P2.Charge()
        P1hpnum = str(int(P1hp)) + "/" + str(P1Bhp)
        P2hpnum = str(int(P2hp)) + "/" + str(P2Bhp)
        P1mpnum = str(int(P1mp)) + "/" + str(P1Bmp)
        P2mpnum = str(int(P2mp)) + "/" + str(P2Bmp)
        P1chargenum = str(int(P1Charge)) + "/" + str(100)
        P2chargenum = str(int(P2Charge)) + "/" + str(100)



    if P1hp == 0:
        P1Dead = True
        P2Dead = False
    elif P2hp == 0:
        P1Dead = False
        P2Dead = True
     
    End = True

    #end
    
    while End:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        
        redrawEndWindow(randBG)

        if keys[pygame.K_SPACE]:
            pygame.time.delay(250)
            End = False
            
        if keys[pygame.K_ESCAPE]:
            pygame.time.delay(250)
            End = False
            run = False
            





pygame.quit()
