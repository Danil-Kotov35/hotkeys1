import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import tkinter
from tkinter import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import re
import design
#import tkinter as tk
from tkinter import ttk
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.start()
        #----------------вызовы функций для изменения горячих клавиш фракции имперской граврдии-----------------
        self.pushChange.clicked.connect(self.change1)
        self.pushChange_2.clicked.connect(self.change2)
        self.pushChange_3.clicked.connect(self.change3)
        self.pushChange_4.clicked.connect(self.change4)
        self.pushChange_5.clicked.connect(self.change5)
        self.pushChange_6.clicked.connect(self.change6)
        self.pushChange_7.clicked.connect(self.change7)
        self.pushChange_8.clicked.connect(self.change8)
        self.pushChange_9.clicked.connect(self.change9)
        self.pushChange_10.clicked.connect(self.change10)
        self.pushChange_11.clicked.connect(self.change11)
        self.pushChange_12.clicked.connect(self.change12)
        self.pushChange_13.clicked.connect(self.change13)
        self.pushChange_14.clicked.connect(self.change14)
        self.pushChange_15.clicked.connect(self.change15)
        self.pushChange_16.clicked.connect(self.change16)
        self.pushChange_17.clicked.connect(self.change17)
        self.pushChange_18.clicked.connect(self.change18)
        self.pushChange_19.clicked.connect(self.change19)
        self.pushChange_20.clicked.connect(self.change20)
        self.pushChange_21.clicked.connect(self.change21)
        self.pushChange_22.clicked.connect(self.change22)
        self.pushChange_23.clicked.connect(self.change23)
        self.pushChange_24.clicked.connect(self.change24)
        self.pushChange_25.clicked.connect(self.change25)
        self.pushChange_26.clicked.connect(self.change26)
        self.pushChange_27.clicked.connect(self.change27)
        self.pushChange_28.clicked.connect(self.change28)
        self.pushChange_29.clicked.connect(self.change29)
        self.pushChange_30.clicked.connect(self.change30)
        self.pushChange_31.clicked.connect(self.change31)
        self.pushChange_32.clicked.connect(self.change32)
        self.pushChange_33.clicked.connect(self.change33)
        self.pushChange_34.clicked.connect(self.change34)
        self.pushChange_35.clicked.connect(self.change35)
        self.pushChange_36.clicked.connect(self.change36)
        self.pushChange_44.clicked.connect(self.change44)
        self.pushChange_45.clicked.connect(self.change45)
        self.pushChange_46.clicked.connect(self.change46)
        self.pushChange_47.clicked.connect(self.change47)
        self.pushChange_48.clicked.connect(self.change48)
        self.pushChange_49.clicked.connect(self.change49)
        self.pushChange_50.clicked.connect(self.change50)
        self.pushChange_51.clicked.connect(self.change51)
        self.pushChange_52.clicked.connect(self.change52)
        self.pushChange_53.clicked.connect(self.change53)
        self.pushChange_54.clicked.connect(self.change54)
        self.pushChange_55.clicked.connect(self.change55)
        self.pushChange_56.clicked.connect(self.change56)
        self.pushChange_57.clicked.connect(self.change57)
        self.pushChange_89.clicked.connect(self.change89)
        self.pushChange_90.clicked.connect(self.change90)
        self.pushChange_58.clicked.connect(self.change58)
        self.pushChange_59.clicked.connect(self.change59)
        self.pushChange_60.clicked.connect(self.change60)
        self.pushChange_61.clicked.connect(self.change61)
        self.pushChange_62.clicked.connect(self.change62)
        self.pushChange_63.clicked.connect(self.change63)
        self.pushChange_64.clicked.connect(self.change64)
        self.pushChange_65.clicked.connect(self.change65)
        self.pushChange_66.clicked.connect(self.change66)
        self.pushChange_67.clicked.connect(self.change67)
        self.pushChange_68.clicked.connect(self.change68)
        self.pushChange_69.clicked.connect(self.change69)
        self.pushChange_70.clicked.connect(self.change70)
        self.pushChange_71.clicked.connect(self.change71)
        self.pushChange_72.clicked.connect(self.change72)
        self.pushChange_73.clicked.connect(self.change73)
        self.pushChange_74.clicked.connect(self.change74)
        self.pushChange_75.clicked.connect(self.change75)
        self.pushChange_76.clicked.connect(self.change76)
        self.pushChange_77.clicked.connect(self.change77)
        self.pushChange_78.clicked.connect(self.change78)
        self.pushChange_79.clicked.connect(self.change79)
        self.pushChange_80.clicked.connect(self.change80)
        self.pushChange_81.clicked.connect(self.change81)
        self.pushChange_82.clicked.connect(self.change82)
        self.pushChange_83.clicked.connect(self.change83)
        self.pushChange_84.clicked.connect(self.change84)
        self.pushChange_85.clicked.connect(self.change85)
        self.pushChange_86.clicked.connect(self.change86)
        self.pushChange_87.clicked.connect(self.change87)
        self.pushChange_88.clicked.connect(self.change88)
        #----------------вызовы функций для изменения горячих клавиш фракции космодесант-----------------
        self.pushChange_91.clicked.connect(self.change91)
        self.pushChange_92.clicked.connect(self.change92)
        self.pushChange_93.clicked.connect(self.change93)
        self.pushChange_94.clicked.connect(self.change94)
        self.pushChange_95.clicked.connect(self.change95)
        self.pushChange_96.clicked.connect(self.change96)
        self.pushChange_97.clicked.connect(self.change97)
        self.pushChange_98.clicked.connect(self.change98)
        self.pushChange_99.clicked.connect(self.change99)
        self.pushChange_100.clicked.connect(self.change100)
        self.pushChange_101.clicked.connect(self.change101)
        self.pushChange_102.clicked.connect(self.change102)
        self.pushChange_103.clicked.connect(self.change103)
        self.pushChange_104.clicked.connect(self.change104)
        self.pushChange_105.clicked.connect(self.change105)
        self.pushChange_106.clicked.connect(self.change106)
        self.pushChange_107.clicked.connect(self.change107)
        self.pushChange_108.clicked.connect(self.change108)
        self.pushChange_109.clicked.connect(self.change109)
        self.pushChange_110.clicked.connect(self.change110)
        self.pushChange_111.clicked.connect(self.change111)
        self.pushChange_112.clicked.connect(self.change112)
        self.pushChange_113.clicked.connect(self.change113)
        self.pushChange_114.clicked.connect(self.change114)
        self.pushChange_115.clicked.connect(self.change115)
        self.pushChange_116.clicked.connect(self.change116)
        self.pushChange_117.clicked.connect(self.change117)
        self.pushChange_118.clicked.connect(self.change118)
        self.pushChange_119.clicked.connect(self.change119)
        self.pushChange_120.clicked.connect(self.change120)
        self.pushChange_121.clicked.connect(self.change121)
        self.pushChange_122.clicked.connect(self.change122)
        self.pushChange_123.clicked.connect(self.change123)
        self.pushChange_124.clicked.connect(self.change124)
        self.pushChange_125.clicked.connect(self.change125)
        self.pushChange_126.clicked.connect(self.change126)
        self.pushChange_127.clicked.connect(self.change127)
        self.pushChange_128.clicked.connect(self.change128)
        self.pushChange_129.clicked.connect(self.change129)
        self.pushChange_130.clicked.connect(self.change130)
        self.pushChange_131.clicked.connect(self.change131)
        self.pushChange_132.clicked.connect(self.change132)
        self.pushChange_133.clicked.connect(self.change133)
        self.pushChange_134.clicked.connect(self.change134)
        self.pushChange_135.clicked.connect(self.change135)
        self.pushChange_136.clicked.connect(self.change136)
        self.pushChange_137.clicked.connect(self.change137)
        self.pushChange_138.clicked.connect(self.change138)
        self.pushChange_139.clicked.connect(self.change139)
        self.pushChange_140.clicked.connect(self.change140)
        self.pushChange_141.clicked.connect(self.change141)
        self.pushChange_142.clicked.connect(self.change142)
        self.pushChange_143.clicked.connect(self.change143)
        self.pushChange_144.clicked.connect(self.change144)
        self.pushChange_145.clicked.connect(self.change145)
        self.pushChange_146.clicked.connect(self.change146)
        self.pushChange_147.clicked.connect(self.change147)
        self.pushChange_148.clicked.connect(self.change148)
        self.pushChange_149.clicked.connect(self.change149)
        self.pushChange_150.clicked.connect(self.change150)
        self.pushChange_151.clicked.connect(self.change151)
        self.pushChange_152.clicked.connect(self.change152)
        self.pushChange_153.clicked.connect(self.change153)
        self.pushChange_154.clicked.connect(self.change154)
        self.pushChange_155.clicked.connect(self.change155)
        self.pushChange_156.clicked.connect(self.change156)
        self.pushChange_157.clicked.connect(self.change157)
        self.pushChange_158.clicked.connect(self.change158)
        self.pushChange_159.clicked.connect(self.change159)
        self.pushChange_160.clicked.connect(self.change160)
        self.pushChange_161.clicked.connect(self.change161)
        self.pushChange_162.clicked.connect(self.change162)
        self.pushChange_163.clicked.connect(self.change163)
        self.pushChange_164.clicked.connect(self.change164)
        self.pushChange_165.clicked.connect(self.change165)
        self.pushChange_166.clicked.connect(self.change166)
        self.pushChange_167.clicked.connect(self.change167)
        self.pushChange_168.clicked.connect(self.change168)
        self.pushChange_169.clicked.connect(self.change169)
        self.pushChange_170.clicked.connect(self.change170)
        self.pushChange_171.clicked.connect(self.change171)
        self.pushChange_172.clicked.connect(self.change172)
        self.pushChange_173.clicked.connect(self.change173)
        self.pushChange_174.clicked.connect(self.change174)
        self.pushChange_175.clicked.connect(self.change175)
        self.pushChange_176.clicked.connect(self.change176)
        self.pushChange_177.clicked.connect(self.change177)
        self.pushChange_178.clicked.connect(self.change178)
        self.pushChange_179.clicked.connect(self.change179)
        self.pushChange_180.clicked.connect(self.change180)
        self.pushChange_181.clicked.connect(self.change181)
        self.pushChange_182.clicked.connect(self.change182)
        self.pushChange_183.clicked.connect(self.change183)
        self.pushChange_184.clicked.connect(self.change184)
        self.pushChange_185.clicked.connect(self.change185)
        self.pushChange_186.clicked.connect(self.change186)
        self.pushChange_187.clicked.connect(self.change187)
        self.pushChange_188.clicked.connect(self.change188)
        self.pushChange_189.clicked.connect(self.change189)
        self.pushChange_190.clicked.connect(self.change190)
        self.pushChange_191.clicked.connect(self.change191)
        self.pushChange_192.clicked.connect(self.change192)
        self.pushChange_193.clicked.connect(self.change193)
        self.pushChange_194.clicked.connect(self.change194)
        self.pushChange_195.clicked.connect(self.change195)
        self.pushChange_196.clicked.connect(self.change196)
        self.pushChange_197.clicked.connect(self.change197)
        self.pushChange_198.clicked.connect(self.change198)
        self.pushChange_199.clicked.connect(self.change199)
        self.pushChange_200.clicked.connect(self.change200)
        self.pushChange_201.clicked.connect(self.change201)
        self.pushChange_202.clicked.connect(self.change202)
        self.pushChange_203.clicked.connect(self.change203)
        self.pushChange_204.clicked.connect(self.change204)
        self.pushChange_205.clicked.connect(self.change205)
        self.pushChange_206.clicked.connect(self.change206)
        self.pushChange_207.clicked.connect(self.change207)
        self.pushChange_208.clicked.connect(self.change208)
        self.pushChange_209.clicked.connect(self.change209)
        self.pushChange_210.clicked.connect(self.change210)
        self.pushChange_211.clicked.connect(self.change211)
        self.pushChange_212.clicked.connect(self.change212)
        self.pushChange_213.clicked.connect(self.change213)
        self.pushChange_214.clicked.connect(self.change214)
        self.pushChange_215.clicked.connect(self.change215)
        self.pushChange_216.clicked.connect(self.change216)
        self.pushChange_217.clicked.connect(self.change217)
        self.pushChange_218.clicked.connect(self.change218)
        self.pushChange_219.clicked.connect(self.change219)
        self.pushChange_220.clicked.connect(self.change220)
        self.pushChange_221.clicked.connect(self.change221)
        self.pushChange_222.clicked.connect(self.change222)
        self.pushChange_223.clicked.connect(self.change223)
        self.pushChange_224.clicked.connect(self.change224)
        self.pushChange_225.clicked.connect(self.change225)
        self.pushChange_226.clicked.connect(self.change226)
        self.pushChange_227.clicked.connect(self.change227)
        self.pushChange_228.clicked.connect(self.change228)
        self.pushChange_229.clicked.connect(self.change229)
        self.pushChange_230.clicked.connect(self.change230)
        self.pushChange_231.clicked.connect(self.change231)
        self.pushChange_232.clicked.connect(self.change232)
        self.pushChange_233.clicked.connect(self.change233)







        #----------------вызовы функций страниц для имперской гвардии---------------------
        self.imperial_guard.clicked.connect(self.IG_menu)
        self.IG_build.clicked.connect(self.IG_subMenu_1)
        
        self.IG_army.clicked.connect(self.IG_subMenu_2)
        self.btn_next_1.clicked.connect(self.IG_subMenu_3)
        self.btn_pred_1.clicked.connect(self.IG_subMenu_2)
        
        self.IG_weapon.clicked.connect(self.IG_subMenu_4)
        
        self.IG_study.clicked.connect(self.IG_subMenu_5)
        self.next_btn_2.clicked.connect(self.IG_subMenu_6)
        self.pred_btn_2.clicked.connect(self.IG_subMenu_5)
        
        self.IG_upgrade.clicked.connect(self.IG_subMenu_7)
        self.next_btn_3.clicked.connect(self.IG_subMenu_8)
        self.pred_btn_3.clicked.connect(self.IG_subMenu_7)

        self.IG_capabilities.clicked.connect(self.IG_subMenu_9)
        self.next_btn_4.clicked.connect(self.IG_subMenu_10)
        self.pred_btn_4.clicked.connect(self.IG_subMenu_9)



        #----------------вызовы функций страниц для космодесанта---------------------

        self.space_marines.clicked.connect(self.SM_menu)
        
        self.SM_build.clicked.connect(self.SM_submenu_1)

        self.SM_army.clicked.connect(self.SM_submenu_2)
        self.next_btn_5.clicked.connect(self.SM_submenu_3)
        self.pred_btn_5.clicked.connect(self.SM_submenu_2)

        self.SM_weapon.clicked.connect(self.SM_submenu_4)
        self.next_btn_6.clicked.connect(self.SM_submenu_5)
        self.pred_btn_6.clicked.connect(self.SM_submenu_4)

        self.SM_study.clicked.connect(self.SM_submenu_6)
        self.next_btn_7.clicked.connect(self.SM_submenu_7)
        self.next_btn_8.clicked.connect(self.SM_submenu_8)
        self.pred_btn_7.clicked.connect(self.SM_submenu_6)
        self.pred_btn_8.clicked.connect(self.SM_submenu_7)

        self.SM_upgrade.clicked.connect(self.SM_submenu_9)

        self.SM_capabilities.clicked.connect(self.SM_submenu_10)

      	#--------------вызовы функций общих значаний---------------

        self.general_commands.clicked.connect(self.generalCom_menu)
      	
        self.G_btn_system.clicked.connect(self.G_submenu_1)

        self.G_btn_task.clicked.connect(self.G_submenu_2)
        self.next_btn_9.clicked.connect(self.G_submenu_3)
        self.next_btn_10.clicked.connect(self.G_submenu_4)
        self.pred_btn_10.clicked.connect(self.G_submenu_3)
        self.pred_btn_9.clicked.connect(self.G_submenu_2)





    		

# ------------------------функции замены для имперской гвардии--------------------------------
    def change1(self):
    	word = "guard_hq"
    	lineEdit = self.line_guard_hq
    	Change_global.Change_global_inner(self,word,lineEdit)
    
    def change2(self):
    	word = "guard_tactica"
    	lineEdit = self.line_guard_tactica
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change3(self):
    	word = "guard_infantry"
    	lineEdit = self.line_guard_infantry
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change4(self):
    	word = "guard_generator"
    	lineEdit = self.line_guard_generator
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change5(self):
    	word = "guard_listening_post"
    	lineEdit = self.line_guard_listening_post
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change6(self):
    	word = "guard_mars_command"
    	lineEdit = self.line_guard_mars_command
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change7(self):
    	word = "guard_thermo_generator"
    	lineEdit = self.line_guard_thermo_generator
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change8(self):
    	word = "guard_bolter_turret"
    	lineEdit = self.line_guard_bolter_turret
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change9(self):
    	word = "guard_mechanized_command"
    	lineEdit = self.line_guard_mechanized_command
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change10(self):
    	word = "guard_mine_field"
    	lineEdit = self.line_guard_mine_field
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change11(self):
    	word = "guard_enginseer"
    	lineEdit = self.line_guard_enginseer
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change12(self):
    	word = "guard_guardsmen"
    	lineEdit = self.line_guard_guardsmen
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change13(self):
    	word = "guard_assassin"
    	lineEdit = self.line_guard_assassin
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change14(self):
    	word = "guard_heavy_weapon"
    	lineEdit = self.line_guard_heavy_weapon
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change15(self):
    	word = "guard_command_squad"
    	lineEdit = self.line_guard_command_squad
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change16(self):
    	word = "guard_commissar"
    	lineEdit = self.line_guard_commissar
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change17(self):
    	word = "guard_priest"
    	lineEdit = self.line_guard_priest
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change18(self):
    	word = "guard_psyker"
    	lineEdit = self.line_guard_psyker
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change19(self):
    	word = "guard_kasrkin"
    	lineEdit = self.line_guard_kasrkin
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change20(self):
    	word = "guard_ogryn"
    	lineEdit = self.line_guard_ogryn
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change21(self):
    	word = "guard_basilisk"
    	lineEdit = self.line_guard_basilisk
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change22(self):
    	word = "guard_sentinel"
    	lineEdit = self.line_guard_hellhound
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change23(self):
    	word = "guard_hellhound"
    	lineEdit = self.line_guard_marauder
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change24(self):
    	word = "guard_marauder"
    	lineEdit = self.line_guard_marauder
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change25(self):
    	word = "guard_baneblade"
    	lineEdit = self.line_guard_baneblade
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change26(self):
    	word = "guard_leman_russ"
    	lineEdit = self.line_guard_leman_russ
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change27(self):
    	word = "guard_chimera"
    	lineEdit = self.line_guard_chimera
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change28(self):
    	word = "guard_sergeant"
    	lineEdit = self.line_guard_sergeant
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change29(self):
    	word = "guard_demolisher"
    	lineEdit = self.line_guard_demolisher
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change30(self):
    	word = "guard_grenade_launcher"
    	lineEdit = self.line_guard_grenade_launcher
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change31(self):
    	word = "guard_plasma_gun"
    	lineEdit = self.line_guard_plasma_gun
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change32(self):
    	word = "guard_lasgun_heavy_weapons_team"
    	lineEdit = self.line_guard_lasgun_heavy_weapons_team
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change33(self):
    	word = "guard_autocannon_heavy_weapons_team"
    	lineEdit = self.line_guard_autocannon_heavy_weapons_team
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change34(self):
    	word = "guard_multi_melta"
    	lineEdit = self.line_guard_multi_melta
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change35(self):
    	word = "guard_multi_laser_sentinel"
    	lineEdit = self.line_guard_multi_laser_sentinel
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change36(self):
    	word = "guard_autocannon_sentinel"
    	lineEdit = self.line_guard_autocannon_sentinel
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change44(self):
    	word = "guard_guardsman_morale"
    	lineEdit = self.line_guard_guardsman_morale
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change45(self):
    	word = "guard_guardsman_morale_2"
    	lineEdit = self.line_guard_guardsman_morale_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change46(self):
    	word = "guard_research_command_squad_size"
    	lineEdit = self.line_guard_research_command_squad_size
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change47(self):
    	word = "guard_research_kasrkin_armor"
    	lineEdit = self.line_guard_research_kasrkin_armor
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change48(self):
    	word = "guard_research_kasrkin_speed"
    	lineEdit = self.line_guard_research_kasrkin_speed
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change49(self):
    	word = "guard_upgrade_guardsmen_health"
    	lineEdit = self.line_guard_upgrade_guardsmen_health
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change50(self):
    	word = "guard_upgrade_guardsmen_range"
    	lineEdit = self.line_guard_upgrade_guardsmen_range
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change51(self):
    	word = "guard_upgrade_ogryn_melee"
    	lineEdit = self.line_guard_upgrade_ogryn_melee
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change52(self):
    	word = "guard_upgrade_power_1"
    	lineEdit = self.line_guard_upgrade_power_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change53(self):
    	word = "guard_upgrade_power_2"
    	lineEdit = self.line_guard_upgrade_power_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change54(self):
    	word = "guard_upgrade_requisition_1"
    	lineEdit = self.line_guard_upgrade_requisition_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change55(self):
    	word = "guard_upgrade_requisition_2"
    	lineEdit = self.line_guard_upgrade_requisition_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change56(self):
    	word = "guard_upgrade_weapon_specialization"
    	lineEdit = self.line_guard_upgrade_weapon_specialization
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change57(self):
    	word = "guard_full_scale_war"
    	lineEdit = self.line_guard_full_scale_war
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change89(self):
    	word = "guard_research_sentinel_armor"
    	lineEdit = self.line_guard_research_sentinel_armor
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change90(self):
    	word = "guard_research_assassin_infiltrate"
    	lineEdit = self.line_guard_research_assassin_infiltrate
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change58(self):
    	word = "addon_guard_basilisk_depot"
    	lineEdit = self.line_addon_guard_basilisk_depot
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change59(self):
    	word = "addon_guard_heavy_weapon_vault"
    	lineEdit = self.line_addon_guard_heavy_weapon_vault
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change60(self):
    	word = "addon_guard_hellhound_depot"
    	lineEdit = self.line_addon_guard_hellhound_depot
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change61(self):
    	word = "addon_guard_hq_1"
    	lineEdit = self.line_addon_guard_hq_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change62(self):
    	word = "addon_guard_hq_2"
    	lineEdit = self.line_addon_guard_hq_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change63(self):
    	word = "addon_guard_kasrkin_quarters"
    	lineEdit = self.line_addon_guard_kasrkin_quarters
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change64(self):
    	word = "addon_guard_leman_russ_depot"
    	lineEdit = self.line_addon_guard_leman_russ_depot
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change65(self):
    	word = "addon_guard_list_post_1"
    	lineEdit = self.line_addon_guard_list_post_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change66(self):
    	word = "addon_guard_list_post_2"
    	lineEdit = self.line_addon_guard_list_post_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change67(self):
    	word = "addon_guard_ministorum_temple"
    	lineEdit = self.line_addon_guard_ministorum_temple
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change68(self):
    	word = "addon_guard_ogryn_quarters"
    	lineEdit = self.line_addon_guard_ogryn_quarters
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change69(self):
    	word = "addon_guard_sentinel_depot"
    	lineEdit = self.line_addon_guard_sentinel_depot
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change70(self):
    	word = "addon_guard_telepathica_temple"
    	lineEdit = self.line_addon_guard_telepathica_temple
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change71(self):
    	word = "addon_guard_vindicare_temple"
    	lineEdit = self.line_addon_guard_vindicare_temple
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change72(self):
    	word = "guard_turret_addon"
    	lineEdit = self.line_guard_turret_addon
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change73(self):
    	word = "addon_guard_demolisher_depot"
    	lineEdit = self.line_addon_guard_demolisher_depot
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change74(self):
    	word = "guard_assassin_assassinate"
    	lineEdit = self.line_guard_assassin_assassinate
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change75(self):
    	word = "earthshaker_round"
    	lineEdit = self.line_earthshaker_round
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change76(self):
    	word = "guard_commissar_execute"
    	lineEdit = self.line_guard_commissar_execute
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change77(self):
    	word = "guard_kasrkin_frag_grenades"
    	lineEdit = self.line_guard_kasrkin_frag_grenades
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change78(self):
    	word = "guard_priest_fanatical"
    	lineEdit = self.line_guard_priest_fanatical
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change79(self):
    	word = "guard_psyker_lighting_arc"
    	lineEdit = self.line_guard_psyker_lighting_arc
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change80(self):
    	word = "guard_psyker_strip_soul"
    	lineEdit = self.line_guard_psyker_strip_soul
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change81(self):
    	word = "guard_strafing_run"
    	lineEdit = self.line_guard_strafing_run
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change82(self):
    	word = "guard_let_it_burn"
    	lineEdit = self.line_guard_let_it_burn
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change83(self):
    	word = "guard_long_range_scanner"
    	lineEdit = self.line_guard_long_range_scanner
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change84(self):
    	word = "guard_curse_of_the_machine"
    	lineEdit = self.line_guard_curse_of_the_machine
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change85(self):
    	word = "guard_incendiary_bombs"
    	lineEdit = self.line_guard_incendiary_bombs
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change86(self):
    	word = "guard_emp_bombs"
    	lineEdit = self.line_guard_emp_bombs
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change87(self):
    	word = "guard_smoke_bombs"
    	lineEdit = self.line_guard_smoke_bombs
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change88(self):
    	word = "guard_krak_bombs"
    	lineEdit = self.line_guard_krak_bombs
    	Change_global.Change_global_inner(self,word,lineEdit)										







#------------------функции замены для космодесанта------------
    def change91(self):
    	word = "marine_hq"
    	lineEdit = self.line_marine_hq
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change92(self):
    	word = "marine_artefact"
    	lineEdit = self.line_marine_artefact
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change93(self):
    	word = "marine_armoury"
    	lineEdit = self.line_marine_armoury
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change94(self):
    	word = "marine_chapel"
    	lineEdit = self.line_marine_chapel
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change95(self):
    	word = "marine_generator"
    	lineEdit = self.line_marine_generator
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change96(self):
    	word = "marine_listening_post"
    	lineEdit = self.line_marine_listening_post
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change97(self):
    	word = "marine_orbital_relay"
    	lineEdit = self.line_marine_orbital_relay
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change98(self):
    	word = "marine_temp_drop_building"
    	lineEdit = self.line_marine_temp_drop_building
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change99(self):
    	word = "marine_thermo_generator"
    	lineEdit = self.line_marine_thermo_generator
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change100(self):
    	word = "marine_bolter_turret"
    	lineEdit = self.line_marine_bolter_turret
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change101(self):
    	word = "marine_machine_cult"
    	lineEdit = self.line_marine_machine_cult
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change102(self):
    	word = "marine_mine_field"
    	lineEdit = self.line_marine_mine_field
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change103(self):
    	word = "marine_servitor"
    	lineEdit = self.line_marine_servitor
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change104(self):
    	word = "marine_dreadnought"
    	lineEdit = self.line_marine_dreadnought
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change105(self):
    	word = "marine_dreadnought_hellfire"
    	lineEdit = self.line_marine_dreadnought_hellfire
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change106(self):
    	word = "marine_force_commander"
    	lineEdit = self.line_marine_force_commander
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change107(self):
    	word = "marine_chaplain"
    	lineEdit = self.line_marine_chaplain
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change108(self):
    	word = "marine_grey_knights"
    	lineEdit = self.line_marine_grey_knights
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change109(self):
    	word = "marine_land_speeder"
    	lineEdit = self.line_marine_land_speeder
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change110(self):
    	word = "marine_librarian"
    	lineEdit = self.line_marine_librarian
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change111(self):
    	word = "marine_skull_probe"
    	lineEdit = self.line_marine_skull_probe
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change112(self):
    	word = "marine_scout"
    	lineEdit = self.line_marine_scout
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change113(self):
    	word = "marine_apothecary"
    	lineEdit = self.line_marine_apothecary
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change114(self):
    	word = "marine_assault_marine"
    	lineEdit = self.line_marine_assault_marine
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change115(self):
    	word = "marine_sergeant"
    	lineEdit = self.line_marine_sergeant
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change116(self):
    	word = "marine_space_marine"
    	lineEdit = self.line_marine_space_marine
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change117(self):
    	word = "marine_terminator"
    	lineEdit = self.line_marine_terminator
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change118(self):
    	word = "marine_assault_terminator"
    	lineEdit = self.line_marine_assault_terminator
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change119(self):
    	word = "marine_land_raider"
    	lineEdit = self.line_marine_land_raider
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change120(self):
    	word = "marine_predator"
    	lineEdit = self.line_marine_predator
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change121(self):
    	word = "marine_rhino"
    	lineEdit = self.line_marine_rhino
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change122(self):
    	word = "marine_whirlwind"
    	lineEdit = self.line_marine_whirlwind
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change123(self):
    	word = "marine_techmarine"
    	lineEdit = self.line_marine_techmarine
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change124(self):
    	word = "marine_tempest"
    	lineEdit = self.line_marine_tempest
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change125(self):
    	word = "marine_assault_cannon"
    	lineEdit = self.line_marine_assault_cannon
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change126(self):
    	word = "marine_flamer"
    	lineEdit = self.line_marine_flamer
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change127(self):
    	word = "marine_heavy_flamer"
    	lineEdit = self.line_marine_heavy_flamer
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change128(self):
    	word = "marine_heavy_bolter"
    	lineEdit = self.line_marine_heavy_bolter
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change129(self):
    	word = "marine_lascannon_1"
    	lineEdit = self.line_marine_lascannon_1
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change130(self):
    	word = "marine_lascannon_2"
    	lineEdit = self.line_marine_lascannon_2
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change131(self):
    	word = "marine_lascannon_twin"
    	lineEdit = self.line_marine_lascannon_twin
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change132(self):
    	word = "marine_missile_launcher"
    	lineEdit = self.line_marine_missile_launcher
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change133(self):
    	word = "marine_plasma_gun"
    	lineEdit = self.line_marine_plasma_gun
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change134(self):
    	word = "marine_sniper_rifle"
    	lineEdit = self.line_marine_sniper_rifle
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change135(self):
    	word = "marine_missile_launcher_turret"
    	lineEdit = self.line_marine_missile_launcher_turret
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change136(self):
    	word = "marine_power_halberd"
    	lineEdit = self.line_marine_power_halberd
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change137(self):
    	word = "marine_missile_frag"
    	lineEdit = self.line_marine_missile_frag
    	Change_global.Change_global_inner(self,word,lineEdit)
    	
    def change138(self):
    	word = "marine_missile_krak"
    	lineEdit = self.line_marine_missile_krak
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change139(self):
    	word = "marine_accuracy_research_1"
    	lineEdit = self.line_marine_accuracy_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change140(self):
    	word = "marine_accuracy_research_2"
    	lineEdit = self.line_marine_accuracy_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change141(self):
    	word = "marine_force_commander_research_1"
    	lineEdit = self.line_marine_force_commander_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change142(self):
    	word = "marine_force_commander_research_2"
    	lineEdit = self.line_marine_force_commander_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change143(self):
    	word = "marine_daemon_hammer_research"
    	lineEdit = self.line_marine_daemon_hammer_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change144(self):
    	word = "marine_frag_grenade_research"
    	lineEdit = self.line_marine_frag_grenade_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change145(self):
    	word = "marine_health_research_1"
    	lineEdit = self.line_marine_health_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change146(self):
    	word = "marine_health_research_2"
    	lineEdit = self.line_marine_health_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change147(self):
    	word = "marine_commander_health_research_1"
    	lineEdit = self.line_marine_commander_health_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change148(self):
    	word = "marine_commander_health_research_2"
    	lineEdit = self.line_marine_commander_health_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change149(self):
    	word = "marine_librarian_research_1"
    	lineEdit = self.line_marine_librarian_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change150(self):
    	word = "marine_librarian_research_2"
    	lineEdit = self.line_marine_librarian_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change151(self):
    	word = "marine_max_weapons_research"
    	lineEdit = self.line_marine_max_weapons_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change152(self):
    	word = "marine_melta_bomb_research"
    	lineEdit = self.line_marine_melta_bomb_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change153(self):
    	word = "marine_power_research_1"
    	lineEdit = self.line_marine_power_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change154(self):
    	word = "marine_power_research_2"
    	lineEdit = self.line_marine_power_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change155(self):
    	word = "marine_requisition_research_1"
    	lineEdit = self.line_marine_requisition_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change156(self):
    	word = "marine_requisition_research_2"
    	lineEdit = self.line_marine_requisition_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change157(self):
    	word = "marine_scout_infiltration_research"
    	lineEdit = self.line_marine_scout_infiltration_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change158(self):
    	word = "marine_smoke_launcher_research"
    	lineEdit = self.line_marine_smoke_launcher_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change159(self):
    	word = "marine_squad_cap_research"
    	lineEdit = self.line_marine_squad_cap_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change160(self):
    	word = "marine_vehicle_cap_research"
    	lineEdit = self.line_marine_vehicle_cap_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change161(self):
    	word = "marine__melee_research_1"
    	lineEdit = self.line_marine__melee_research_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change162(self):
    	word = "marine_sergeant_melee_research_2"
    	lineEdit = self.line_marine_sergeant_melee_research_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change163(self):
    	word = "marine_sergeant_ranged_research"
    	lineEdit = self.line_marine_sergeant_ranged_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change164(self):
    	word = "marine_personalteleporter_research"
    	lineEdit = self.line_marine_personalteleporter_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change165(self):
    	word = "marine_heavy_armor_deployment"
    	lineEdit = self.line_marine_heavy_armor_deployment
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change166(self):
    	word = "marine_furious_charge_research"
    	lineEdit = self.line_marine_furious_charge_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change167(self):
    	word = "marine_power_swords_research"
    	lineEdit = self.line_marine_power_swords_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change168(self):
    	word = "marine_skull_probe_infiltration_research"
    	lineEdit = self.line_marine_skull_probe_infiltration_research
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change169(self):
    	word = "marine_hq_addon_1"
    	lineEdit = self.line_marine_hq_addon_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change170(self):
    	word = "marine_hq_addon_2"
    	lineEdit = self.line_marine_hq_addon_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change171(self):
    	word = "marine_listening_post_1"
    	lineEdit = self.line_marine_listening_post_1
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change172(self):
    	word = "marine_listening_post_2"
    	lineEdit = self.line_marine_listening_post_2
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change173(self):
    	word = "marine_turret_addon"
    	lineEdit = self.line_marine_turret_addon
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change174(self):
    	word = "marine_battlecry"
    	lineEdit = self.line_marine_battlecry
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change175(self):
    	word = "marine_demoralize"
    	lineEdit = self.line_marine_demoralize
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change176(self):
    	word = "marine_frag_grenades"
    	lineEdit = self.line_marine_frag_grenades
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change177(self):
    	word = "marine_machine_spirit"
    	lineEdit = self.line_marine_machine_spirit
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change178(self):
    	word = "marine_melta_bombs"
    	lineEdit = self.line_marine_melta_bombs
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change179(self):
    	word = "marine_orbital_bombardment"
    	lineEdit = self.line_marine_orbital_bombardment
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change180(self):
    	word = "marine_rally"
    	lineEdit = self.line_marine_rally
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change181(self):
    	word = "marine_sabotage"
    	lineEdit = self.line_marine_sabotage
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change182(self):
    	word = "marine_smite"
    	lineEdit = self.line_marine_smite
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change183(self):
    	word = "marine_smoke_launchers"
    	lineEdit = self.line_marine_smoke_launchers
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change184(self):
    	word = "marine_weaken_resolve"
    	lineEdit = self.line_marine_weaken_resolve
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change185(self):
    	word = "marine_word_of_emperer"
    	lineEdit = self.line_marine_word_of_emperer
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change186(self):
    	word = "marine_inquisition"
    	lineEdit = self.line_marine_inquisition
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change187(self):
    	word = "marine_blessing_of_the_omnissiah"
    	lineEdit = self.line_marine_blessing_of_the_omnissiah
    	Change_global.Change_global_inner(self,word,lineEdit)




    #-------------функции замены для общих команд---------------
    def change188(self):
    	word = "escape"
    	lineEdit = self.line_escape
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change189(self):
    	word = "accept"
    	lineEdit = self.line_accept
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change190(self):
    	word = "commandqueue"
    	lineEdit = self.line_commandqueue
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change191(self):
    	word = "systemmenu"
    	lineEdit = self.line_systemmenu
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change192(self):
    	word = "objectivesmenu"
    	lineEdit = self.line_objectivesmenu
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change193(self):
    	word = "alliesmenu"
    	lineEdit = self.line_alliesmenu
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change194(self):
    	word = "chatmenu"
    	lineEdit = self.line_chatmenu
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change195(self):
    	word = "pause"
    	lineEdit = self.line_pause
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change196(self):
    	word = "selectionfocus"
    	lineEdit = self.line_selectionfocus
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change197(self):
    	word = "stop"
    	lineEdit = self.line_stop
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change198(self):
    	word = "move"
    	lineEdit = self.line_move
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change199(self):
    	word = "attackmove"
    	lineEdit = self.line_attackmove
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change200(self):
    	word = "attackmelee"
    	lineEdit = self.line_attackmelee
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change201(self):
    	word = "build"
    	lineEdit = self.line_build
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change202(self):
    	word = "buildadv"
    	lineEdit = self.line_buildadv
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change203(self):
    	word = "attach"
    	lineEdit = self.line_attach
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change204(self):
    	word = "jump"
    	lineEdit = self.line_jump
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change205(self):
    	word = "rally"
    	lineEdit = self.line_rally
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change206(self):
    	word = "combatstance"
    	lineEdit = self.line_combatstance
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change207(self):
    	word = "meleestance"
    	lineEdit = self.line_meleestance
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change208(self):
    	word = "scuttle"
    	lineEdit = self.line_scuttle
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change209(self):
    	word = "infiltrate"
    	lineEdit = self.line_infiltrate
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change210(self):
    	word = "unload"
    	lineEdit = self.line_unload
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change211(self):
    	word = "deepstrike"
    	lineEdit = self.line_deepstrike
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change212(self):
    	word = "reinforce"
    	lineEdit = self.line_reinforce
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change213(self):
    	word = "leader"
    	lineEdit = self.line_leader
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change214(self):
    	word = "cancelconstruction"
    	lineEdit = self.line_cancelconstruction
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change215(self):
    	word = "rampage"
    	lineEdit = self.line_rampage
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change216(self):
    	word = "repair"
    	lineEdit = self.line_repair
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change217(self):
    	word = "possess"
    	lineEdit = self.line_possess
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change218(self):
    	word = "relocate"
    	lineEdit = self.line_relocate
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change219(self):
    	word = "cannibalism"
    	lineEdit = self.line_cannibalism
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change220(self):
    	word = "possess_enemy"
    	lineEdit = self.line_possess_enemy
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change221(self):
    	word = "fear"
    	lineEdit = self.line_fear
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change222(self):
    	word = "tau_snare_trap"
    	lineEdit = self.line_tau_snare_trap
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change223(self):
    	word = "necron_solar_pulse"
    	lineEdit = self.line_necron_solar_pulse
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change224(self):
    	word = "tau_holographic_projection"
    	lineEdit = self.line_tau_holographic_projection
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change225(self):
    	word = "direct_spawn"
    	lineEdit = self.line_direct_spawn
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change226(self):
    	word = "necron_stasis_field"
    	lineEdit = self.line_necron_stasis_field
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change227(self):
    	word = "entrench"
    	lineEdit = self.line_entrench
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change228(self):
    	word = "burrow"
    	lineEdit = self.line_burrow
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change229(self):
    	word = "lightning_field"
    	lineEdit = self.line_lightning_field
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change230(self):
    	word = "direct_spawn_rally"
    	lineEdit = self.line_direct_spawn_rally
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change231(self):
    	word = "melee_dance"
    	lineEdit = self.line_melee_dance
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change232(self):
    	word = "harvest"
    	lineEdit = self.line_harvest
    	Change_global.Change_global_inner(self,word,lineEdit)

    def change233(self):
    	word = "attackground"
    	lineEdit = self.line_attackground
    	Change_global.Change_global_inner(self,word,lineEdit)










    


    #--------------функции имперской гвардии--------------

    def start(self):
        self.stackedWidget.setCurrentIndex(0)

    def IG_menu(self):
        self.stackedWidget.setCurrentIndex(1)
        self.imperial_guard.setStyleSheet("background:#4E535C;color:#BABBBF;")
        self.space_marines.setStyleSheet("background:#2E3136;")
        self.general_commands.setStyleSheet("background:#2E3136;")
    
    def IG_subMenu_1(self):
        self.stackedWidget_2.setCurrentIndex(1)
        self.IG_build.setStyleSheet("background:#4E535C;color:#BABBBF;") 
        self.IG_army.setStyleSheet("background:#2E3136;")
        self.IG_weapon.setStyleSheet("background:#2E3136;") 
        self.IG_study.setStyleSheet("background:#2E3136;") 
        self.IG_upgrade.setStyleSheet("background:#2E3136;") 
        self.IG_capabilities.setStyleSheet("background:#2E3136;") 
        Base_line.base_line_IG_build(self)
    
    def IG_subMenu_2(self):
        self.stackedWidget_2.setCurrentIndex(2)
        Base_line.base_line_IG_army(self)
        self.IG_build.setStyleSheet("background:#2E3136;") 
        self.IG_army.setStyleSheet("background:#4E535C;color:#BABBBF;")
        self.IG_weapon.setStyleSheet("background:#2E3136;") 
        self.IG_study.setStyleSheet("background:#2E3136;") 
        self.IG_upgrade.setStyleSheet("background:#2E3136;") 
        self.IG_capabilities.setStyleSheet("background:#2E3136;")
    def IG_subMenu_3(self):
        self.stackedWidget_2.setCurrentIndex(3)
        Base_line.base_line_IG_army(self)
    
    def IG_subMenu_4(self):
        self.stackedWidget_2.setCurrentIndex(4)
        Base_line.base_line_IG_weapon(self)
        self.IG_build.setStyleSheet("background:#2E3136;") 
        self.IG_army.setStyleSheet("background:#2E3136;")
        self.IG_weapon.setStyleSheet("background:#4E535C; color:#BABBBF;") 
        self.IG_study.setStyleSheet("background:#2E3136;") 
        self.IG_upgrade.setStyleSheet("background:#2E3136;") 
        self.IG_capabilities.setStyleSheet("background:#2E3136;")
    
    def IG_subMenu_5(self):
        self.stackedWidget_2.setCurrentIndex(5)
        Base_line.base_line_IG_research(self)
        self.IG_build.setStyleSheet("background:#2E3136;") 
        self.IG_army.setStyleSheet("background:#2E3136;")
        self.IG_weapon.setStyleSheet("background:#2E3136;") 
        self.IG_study.setStyleSheet("background:#4E535C; color:#BABBBF;") 
        self.IG_upgrade.setStyleSheet("background:#2E3136;") 
        self.IG_capabilities.setStyleSheet("background:#2E3136;")
    def IG_subMenu_6(self):
        self.stackedWidget_2.setCurrentIndex(6)
        Base_line.base_line_IG_research(self)
    
    def IG_subMenu_7(self):
        self.stackedWidget_2.setCurrentIndex(7)
        Base_line.base_line_IG_upgrades(self)
        self.IG_build.setStyleSheet("background:#2E3136;") 
        self.IG_army.setStyleSheet("background:#2E3136;")
        self.IG_weapon.setStyleSheet("background:#2E3136;") 
        self.IG_study.setStyleSheet("background:#2E3136;") 
        self.IG_upgrade.setStyleSheet("background:#4E535C; color:#BABBBF;") 
        self.IG_capabilities.setStyleSheet("background:#2E3136;")        
    def IG_subMenu_8(self):
        self.stackedWidget_2.setCurrentIndex(8)
        Base_line.base_line_IG_upgrades(self)

    def IG_subMenu_9(self):
        self.stackedWidget_2.setCurrentIndex(9) 
        Base_line.base_line_IG_ability(self)
        self.IG_build.setStyleSheet("background:#2E3136;") 
        self.IG_army.setStyleSheet("background:#2E3136;")
        self.IG_weapon.setStyleSheet("background:#2E3136;") 
        self.IG_study.setStyleSheet("background:#2E3136;") 
        self.IG_upgrade.setStyleSheet("background:#2E3136") 
        self.IG_capabilities.setStyleSheet("background:#4E535C; color:#BABBBF;")    
    def IG_subMenu_10(self):
        self.stackedWidget_2.setCurrentIndex(10)
        Base_line.base_line_IG_ability(self)
    def IG_subMenu_11(self):
        self.stackedWidget_2.setCurrentIndex(11) 


   	#--------------функции космодесанта--------------       
    def SM_menu(self):
        self.stackedWidget.setCurrentIndex(2)
        self.imperial_guard.setStyleSheet("background:#2E3136;")
        self.space_marines.setStyleSheet("background:#4E535C;color:#BABBBF;")
        self.general_commands.setStyleSheet("background:#2E3136;")

    def SM_submenu_1(self):
        self.stackedWidget_3.setCurrentIndex(1)
        Base_line.base_line_SM_build(self)
        self.SM_build.setStyleSheet("background:#4E535C;color:#BABBBF;") 
        self.SM_army.setStyleSheet("background:#2E3136;")
        self.SM_weapon.setStyleSheet("background:#2E3136;") 
        self.SM_study.setStyleSheet("background:#2E3136;") 
        self.SM_upgrade.setStyleSheet("background:#2E3136;") 
        self.SM_capabilities.setStyleSheet("background:#2E3136;")
    
    def SM_submenu_2(self):
        self.stackedWidget_3.setCurrentIndex(2)
        Base_line.base_line_SM_army(self)
        self.SM_build.setStyleSheet("background:#2E3136;") 
        self.SM_army.setStyleSheet("background:#4E535C;color:#BABBBF;")
        self.SM_weapon.setStyleSheet("background:#2E3136;") 
        self.SM_study.setStyleSheet("background:#2E3136;") 
        self.SM_upgrade.setStyleSheet("background:#2E3136;") 
        self.SM_capabilities.setStyleSheet("background:#2E3136;")
    
    def SM_submenu_3(self):
        self.stackedWidget_3.setCurrentIndex(3)
        Base_line.base_line_SM_weapon(self)
        
    def SM_submenu_4(self):
        self.stackedWidget_3.setCurrentIndex(4)
        Base_line.base_line_SM_weapon(self)
        self.SM_build.setStyleSheet("background:#2E3136;") 
        self.SM_army.setStyleSheet("background:#2E3136;")
        self.SM_weapon.setStyleSheet("background:#4E535C; color:#BABBBF;") 
        self.SM_study.setStyleSheet("background:#2E3136;") 
        self.SM_upgrade.setStyleSheet("background:#2E3136;") 
        self.SM_capabilities.setStyleSheet("background:#2E3136;")
    
    def SM_submenu_5(self):
        self.stackedWidget_3.setCurrentIndex(5)
        Base_line.base_line_SM_research(self)
        
    def SM_submenu_6(self):
        self.stackedWidget_3.setCurrentIndex(6)
        Base_line.base_line_SM_research(self)
        self.SM_build.setStyleSheet("background:#2E3136;") 
        self.SM_army.setStyleSheet("background:#2E3136;")
        self.SM_weapon.setStyleSheet("background:#2E3136;") 
        self.SM_study.setStyleSheet("background:#4E535C; color:#BABBBF;") 
        self.SM_upgrade.setStyleSheet("background:#2E3136;") 
        self.SM_capabilities.setStyleSheet("background:#2E3136;")
    def SM_submenu_7(self):
    	self.stackedWidget_3.setCurrentIndex(7)
    	Base_line.base_line_SM_research(self)
    
    def SM_submenu_8(self):
    	self.stackedWidget_3.setCurrentIndex(8)
    	
    def SM_submenu_9(self):
        self.stackedWidget_3.setCurrentIndex(9)
        Base_line.base_line_SM_upgrade(self)
        self.SM_build.setStyleSheet("background:#2E3136;") 
        self.SM_army.setStyleSheet("background:#2E3136;")
        self.SM_weapon.setStyleSheet("background:#2E3136;") 
        self.SM_study.setStyleSheet("background:#2E3136;") 
        self.SM_upgrade.setStyleSheet("background:#4E535C; color:#BABBBF;") 
        self.SM_capabilities.setStyleSheet("background:#2E3136")

    def SM_submenu_10(self):
        self.stackedWidget_3.setCurrentIndex(10)
        Base_line.base_line_SM_ability(self)
        self.SM_build.setStyleSheet("background:#2E3136;") 
        self.SM_army.setStyleSheet("background:#2E3136;")
        self.SM_weapon.setStyleSheet("background:#2E3136;") 
        self.SM_study.setStyleSheet("background:#2E3136;") 
        self.SM_upgrade.setStyleSheet("background:#2E3136") 
        self.SM_capabilities.setStyleSheet("background:#4E535C; color:#BABBBF;")
    def SM_submenu_11(self):
    	self.stackedWidget_3.setCurrentIndex(11)
    def SM_submenu_12(self):
    	self.stackedWidget_3.setCurrentIndex(12)


    #----------функции общих команд--------------------

    def generalCom_menu(self):
    	self.stackedWidget.setCurrentIndex(3)
    	self.imperial_guard.setStyleSheet("background:#2E3136;")
    	self.space_marines.setStyleSheet("background:#2E3136;")
    	self.general_commands.setStyleSheet("background:#4E535C;color:#BABBBF;")

    def G_submenu_1(self):
    	self.stackedWidget_4.setCurrentIndex(1)
    	Base_line.base_line_G_command(self)
    	self.G_btn_system.setStyleSheet("background:#4E535C; color:#BABBBF;")
    	self.G_btn_task.setStyleSheet("background:#2E3136;")

    def G_submenu_2(self):
    	self.stackedWidget_4.setCurrentIndex(2)
    	Base_line.base_line_G_command(self)
    	self.G_btn_system.setStyleSheet("background:#2E3136;")
    	self.G_btn_task.setStyleSheet("background:#4E535C; color:#BABBBF;")


    def G_submenu_3(self):
    	self.stackedWidget_4.setCurrentIndex(3)
    	Base_line.base_line_G_command(self)


    def G_submenu_4(self):
    	self.stackedWidget_4.setCurrentIndex(4)
    	Base_line.base_line_G_command(self)




class Search_global(object):
    """docstring for Search_global"""
    def __init__(self, word,lineEdit):
	    super(Search_global, self).__init__()
	    self.word = word
	    self.lineEdit = lineEdit
	    #self.new_data = new_data

    def IG_line_show(self,word,lineEdit):
        Search_global.search_now(self,word)
        self.lineEdit.setText(a)

    

		
    def search_line(self,word,lineEdit):
        Input_key.pop_up_window(self)
        self.lineEdit.setText(text)
        with open("KEYDEFAULTS.LUA", "r") as file:
            for line in file:
                list_words = line.split()
                if word in list_words:
                    b = '"'+text+'"' #так будет записываться новая горячая клавиша
                    result = re.findall(r'"\w+"',line)
                    key = result[0]
                    c = re.sub( key,b,line) #запись новой строки с помощью библиотеки RegEx
                    self.lineEdit.setText(key)
                    data = open('KEYDEFAULTS.LUA', 'r')
                    new_data = data.read().replace(line,c) #замена строки в документе
                    break
        with open("KEYDEFAULTS.LUA", "w") as file:
            file.write(new_data)
        Search_global.IG_line_show(self,word,lineEdit)
    


    def search_now(self,word):
        with open("KEYDEFAULTS.LUA", "r") as file:
            global line
            global a
            for line in file:
                list_words = line.split()
                if word in list_words:
                    l = line.split('"')[1::2]
                    print(line,end='')
                    a = l[0]   

    

class Input_key(object):
	"""docstring for Input_key"""
	def __init__(self):
		super(Input_key, self).__init__()

	def pop_up_window(self):
		def close_window(event):
			global text
			window.destroy()
			text = ', '.join(map(str,[event.keysym]))
			
			if text == "Shift_L":
				text = "Shift"
			elif text == "Shift_R":
				text = "Shift"
			elif text == "Control_R":
				text = "Control"
			elif text == "Control_L":
				text = "Control"
			elif text == "Caps_Lock":
				text = "CapsLock"
			elif text == "Alt_L":
				text = "Alt"
			elif text == "Alt_R":
				text = "Alt"
			elif text == "Return":
				text = "Enter"
			elif re.findall(r'[^a-zA-Z0-9]',text):# фильтр
				text = "change_lang"
				


		
		window = tkinter.Tk()
		label = tkinter.Label(window, text="назначте новую клавишу")
		window.eval('tk::PlaceWindow . center')#расположения окна по центру
		label.pack()
		window.bind("<KeyPress>", close_window)
		window.geometry("180x60")
		window.mainloop()
		print(text)

		
			



class Change_global(object):
	"""docstring for Change_global"""
	def __init__(self):
		super(Change_global, self).__init__()
		
	def Change_global_inner(self,word,lineEdit):
		s = Search_global(word,lineEdit)
		s.IG_line_show(word,lineEdit)
		s.search_line(word,lineEdit)
		s.search_now(word)
		


class Base_line(object):
	"""docstring for Base_line"""
	def __init__(self,arg,build_IG,command_build_IG):
		super(Base_line, self).__init__()
		self.arg = arg 
		self.build_IG = build_IG
		self.command_build_IG = command_build_IG
#------------------ база имперской гвардии--------------------
	def base_line_IG_build(self):

		key = [
		"guard_hq",
		"guard_tactica",
		"guard_infantry",
		"guard_generator",
		"guard_listening_post",
		"guard_mars_command",
		"guard_thermo_generator",
		"guard_bolter_turret",
		"guard_mechanized_command",
		"guard_mine_field"]

		command = [
		self.line_guard_hq,
		self.line_guard_tactica,
		self.line_guard_infantry,
		self.line_guard_generator,
		self.line_guard_listening_post,
		self.line_guard_mars_command,
		self.line_guard_thermo_generator,
		self.line_guard_bolter_turret,
		self.line_guard_mechanized_command,
		self.line_guard_mine_field]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)
			
	
	def base_line_IG_army(self):

		key = [
		"guard_enginseer",
		"guard_guardsmen",
		"guard_heavy_weapon",
		"guard_command_squad",
		"guard_commissar",
		"guard_priest",
		"guard_psyker",
		"guard_kasrkin",
		"guard_ogryn",
		"guard_basilisk",
		"guard_sentinel",
		"guard_hellhound",
		"guard_assassin",
		"guard_baneblade",
		"guard_leman_russ",
		"guard_chimera",
		"guard_sergeant",
		"guard_demolisher",
		"guard_marauder",]

		command = [
		self.line_guard_enginseer,
		self.line_guard_guardsmen,
		self.line_guard_heavy_weapon,
		self.line_guard_command_squad,
		self.line_guard_commissar,
		self.line_guard_priest,
		self.line_guard_psyker,
		self.line_guard_kasrkin,
		self.line_guard_ogryn,
		self.line_guard_basilisk,
		self.line_guard_sentinel,
		self.line_guard_hellhound,
		self.line_guard_assassin,
		self.line_guard_baneblade,
		self.line_guard_leman_russ,
		self.line_guard_chimera,
		self.line_guard_sergeant,
		self.line_guard_demolisher,
		self.line_guard_marauder,]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)


	def base_line_IG_weapon(self):
		key = [
		"guard_grenade_launcher",
		"guard_plasma_gun",
		"guard_lasgun_heavy_weapons_team",
		"guard_autocannon_heavy_weapons_team",
		"guard_multi_melta",
		"guard_multi_laser_sentinel",
		"guard_autocannon_sentinel",]
		command = [
		self.line_guard_grenade_launcher,
		self.line_guard_plasma_gun,
		self.line_guard_lasgun_heavy_weapons_team,
		self.line_guard_autocannon_heavy_weapons_team,
		self.line_guard_multi_melta,
		self.line_guard_multi_laser_sentinel,
		self.line_guard_autocannon_sentinel,]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_IG_research(self):
		key = [
		"guard_guardsman_morale",
		"guard_guardsman_morale_2",
		"guard_research_command_squad_size",
		"guard_research_kasrkin_armor",
		"guard_research_kasrkin_speed",
		"guard_upgrade_guardsmen_health",
		"guard_upgrade_guardsmen_range",
		"guard_upgrade_ogryn_melee",
		"guard_upgrade_power_1",
		"guard_upgrade_power_2",
		"guard_upgrade_requisition_1",
		"guard_upgrade_requisition_2",
		"guard_upgrade_weapon_specialization",
		"guard_full_scale_war",
		"guard_research_sentinel_armor",
		"guard_research_assassin_infiltrate",]
		command = [
		self.line_guard_guardsman_morale,
		self.line_guard_guardsman_morale_2,
		self.line_guard_research_command_squad_size,
		self.line_guard_research_kasrkin_armor,
		self.line_guard_research_kasrkin_speed,
		self.line_guard_upgrade_guardsmen_health,
		self.line_guard_upgrade_guardsmen_range,
		self.line_guard_upgrade_ogryn_melee,
		self.line_guard_upgrade_power_1,
		self.line_guard_upgrade_power_2,
		self.line_guard_upgrade_requisition_1,
		self.line_guard_upgrade_requisition_2,
		self.line_guard_upgrade_weapon_specialization,
		self.line_guard_full_scale_war,
		self.line_guard_research_sentinel_armor,
		self.line_guard_research_assassin_infiltrate,]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_IG_upgrades(self):
		key = [
		"addon_guard_basilisk_depot",
		"addon_guard_heavy_weapon_vault",
		"addon_guard_hellhound_depot",
		"addon_guard_hq_1",
		"addon_guard_hq_2",
		"addon_guard_kasrkin_quarters",
		"addon_guard_leman_russ_depot",
		"addon_guard_list_post_1",
		"addon_guard_list_post_2",
		"addon_guard_ministorum_temple",
		"addon_guard_ogryn_quarters",
		"addon_guard_sentinel_depot",
		"addon_guard_telepathica_temple",
		"addon_guard_vindicare_temple",
		"guard_turret_addon",
		"addon_guard_demolisher_depot",]
		command = [
		self.line_addon_guard_basilisk_depot,
		self.line_addon_guard_heavy_weapon_vault,
		self.line_addon_guard_hellhound_depot,
		self.line_addon_guard_hq_1,
		self.line_addon_guard_hq_2,
		self.line_addon_guard_kasrkin_quarters,
		self.line_addon_guard_leman_russ_depot,
		self.line_addon_guard_list_post_1,
		self.line_addon_guard_list_post_2,
		self.line_addon_guard_ministorum_temple,
		self.line_addon_guard_ogryn_quarters,
		self.line_addon_guard_sentinel_depot,
		self.line_addon_guard_telepathica_temple,
		self.line_addon_guard_vindicare_temple,
		self.line_guard_turret_addon,
		self.line_addon_guard_demolisher_depot]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_IG_ability(self):
		key = [
		"guard_assassin_assassinate",
		"earthshaker_round",
		"guard_commissar_execute",
		"guard_kasrkin_frag_grenades",
		"guard_priest_fanatical",
		"guard_psyker_lighting_arc",
		"guard_psyker_strip_soul",
		"guard_strafing_run",
		"guard_let_it_burn",
		"guard_long_range_scanner",
		"guard_curse_of_the_machine",
		"guard_incendiary_bombs",
		"guard_emp_bombs",
		"guard_smoke_bombs",
		"guard_krak_bombs"]
		command = [
		self.line_guard_assassin_assassinate,
		self.line_earthshaker_round,
		self.line_guard_commissar_execute,
		self.line_guard_kasrkin_frag_grenades,
		self.line_guard_priest_fanatical,
		self.line_guard_psyker_lighting_arc,
		self.line_guard_psyker_strip_soul,
		self.line_guard_strafing_run,
		self.line_guard_let_it_burn,
		self.line_guard_long_range_scanner,
		self.line_guard_curse_of_the_machine,
		self.line_guard_incendiary_bombs,
		self.line_guard_emp_bombs,
		self.line_guard_smoke_bombs,
		self.line_guard_krak_bombs]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)
#------------------ база космодесанта--------------------------
	def base_line_SM_build(self):
		key = [
		"marine_hq",
		"marine_artefact",
		"marine_armoury",
		"marine_chapel",
		"marine_generator",
		"marine_listening_post",
		"marine_orbital_relay",
		"marine_temp_drop_building",
		"marine_thermo_generator",
		"marine_bolter_turret",
		"marine_machine_cult",
		"marine_mine_field",]
		command = [
		self.line_marine_hq,
		self.line_marine_artefact,
		self.line_marine_armoury,
		self.line_marine_chapel,
		self.line_marine_generator,
		self.line_marine_listening_post,
		self.line_marine_orbital_relay,
		self.line_marine_temp_drop_building,
		self.line_marine_thermo_generator,
		self.line_marine_bolter_turret,
		self.line_marine_machine_cult,
		self.line_marine_mine_field,]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_SM_army(self):
		key = [
		"marine_servitor",
		"marine_dreadnought",
		"marine_dreadnought_hellfire",
		"marine_force_commander",
		"marine_chaplain",
		"marine_grey_knights",
		"marine_land_speeder",
		"marine_librarian",
		"marine_skull_probe",
		"marine_scout",
		"marine_apothecary",
		"marine_assault_marine",
		"marine_sergeant",
		"marine_space_marine",
		"marine_terminator",
		"marine_assault_terminator",
		"marine_land_raider",
		"marine_predator",
		"marine_rhino",
		"marine_whirlwind",
		"marine_techmarine",
		"marine_tempest"]
		command = [
		self.line_marine_servitor,
		self.line_marine_dreadnought,
		self.line_marine_dreadnought_hellfire,
		self.line_marine_force_commander,
		self.line_marine_chaplain,
		self.line_marine_grey_knights,
		self.line_marine_land_speeder,
		self.line_marine_librarian,
		self.line_marine_skull_probe,
		self.line_marine_scout,
		self.line_marine_apothecary,
		self.line_marine_assault_marine,
		self.line_marine_sergeant,
		self.line_marine_space_marine,
		self.line_marine_terminator,
		self.line_marine_assault_terminator,
		self.line_marine_land_raider,
		self.line_marine_predator,
		self.line_marine_rhino,
		self.line_marine_whirlwind,
		self.line_marine_techmarine,
		self.line_marine_tempest]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_SM_weapon(self):
		key = [
		"marine_assault_cannon",
		"marine_flamer",
		"marine_heavy_flamer",
		"marine_heavy_bolter",
		"marine_lascannon_1",
		"marine_lascannon_2",
		"marine_lascannon_twin",
		"marine_missile_launcher",
		"marine_plasma_gun",
		"marine_sniper_rifle",
		"marine_missile_launcher_turret",
		"marine_power_halberd",
		"marine_missile_frag",
		"marine_missile_krak",]

		command = [
		self.line_marine_assault_cannon,
		self.line_marine_flamer,
		self.line_marine_heavy_flamer,
		self.line_marine_heavy_bolter,
		self.line_marine_lascannon_1,
		self.line_marine_lascannon_2,
		self.line_marine_lascannon_twin,
		self.line_marine_missile_launcher,
		self.line_marine_plasma_gun,
		self.line_marine_sniper_rifle,
		self.line_marine_missile_launcher_turret,
		self.line_marine_power_halberd,
		self.line_marine_missile_frag,
		self.line_marine_missile_krak]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_SM_research(self):
		key = [
		"marine_accuracy_research_1",
		"marine_accuracy_research_2",
		"marine_force_commander_research_1",
		"marine_force_commander_research_2",
		"marine_daemon_hammer_research",
		"marine_frag_grenade_research",
		"marine_health_research_1",
		"marine_health_research_2",
		"marine_commander_health_research_1",
		"marine_commander_health_research_2",
		"marine_librarian_research_1",
		"marine_librarian_research_2",
		"marine_max_weapons_research",
		"marine_melta_bomb_research",
		"marine_power_research_1",
		"marine_power_research_2",
		"marine_requisition_research_1",
		"marine_requisition_research_2",
		"marine_scout_infiltration_research",
		"marine_smoke_launcher_research",
		"marine_squad_cap_research",
		"marine_vehicle_cap_research",
		"marine__melee_research_1",
		"marine_sergeant_melee_research_2",
		"marine_sergeant_ranged_research",
		"marine_personalteleporter_research",
		"marine_heavy_armor_deployment",
		"marine_furious_charge_research",
		"marine_power_swords_research",
		"marine_skull_probe_infiltration_research"]
		command = [
		self.line_marine_accuracy_research_1,
		self.line_marine_accuracy_research_2,
		self.line_marine_force_commander_research_1,
		self.line_marine_force_commander_research_2,
		self.line_marine_daemon_hammer_research,
		self.line_marine_frag_grenade_research,
		self.line_marine_health_research_1,
		self.line_marine_health_research_2,
		self.line_marine_commander_health_research_1,
		self.line_marine_commander_health_research_2,
		self.line_marine_librarian_research_1,
		self.line_marine_librarian_research_2,
		self.line_marine_max_weapons_research,
		self.line_marine_melta_bomb_research,
		self.line_marine_power_research_1,
		self.line_marine_power_research_2,
		self.line_marine_requisition_research_1,
		self.line_marine_requisition_research_2,
		self.line_marine_scout_infiltration_research,
		self.line_marine_smoke_launcher_research,
		self.line_marine_squad_cap_research,
		self.line_marine_vehicle_cap_research,
		self.line_marine__melee_research_1,
		self.line_marine_sergeant_melee_research_2,
		self.line_marine_sergeant_ranged_research,
		self.line_marine_personalteleporter_research,
		self.line_marine_heavy_armor_deployment,
		self.line_marine_furious_charge_research,
		self.line_marine_power_swords_research,
		self.line_marine_skull_probe_infiltration_research]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def base_line_SM_upgrade(self):
		key = [
		"marine_hq_addon_1",
		"marine_hq_addon_2",
		"marine_listening_post_1",
		"marine_listening_post_2",
		"marine_turret_addon"]

		command = [
		self.line_marine_hq_addon_1,
		self.line_marine_hq_addon_2,
		self.line_marine_listening_post_1,
		self.line_marine_listening_post_2,
		self.line_marine_turret_addon]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)


	def base_line_SM_ability(self):
		key = [
		"marine_battlecry",
		"marine_demoralize",
		"marine_frag_grenades",
		"marine_machine_spirit",
		"marine_melta_bombs",
		"marine_orbital_bombardment",
		"marine_rally",
		"marine_sabotage",
		"marine_smite",
		"marine_smoke_launchers",
		"marine_weaken_resolve",
		"marine_word_of_emperer",
		"marine_inquisition",
		"marine_blessing_of_the_omnissiah"]

		command = [
		self.line_marine_battlecry,
		self.line_marine_demoralize,
		self.line_marine_frag_grenades,
		self.line_marine_machine_spirit,
		self.line_marine_melta_bombs,
		self.line_marine_orbital_bombardment,
		self.line_marine_rally,
		self.line_marine_sabotage,
		self.line_marine_smite,
		self.line_marine_smoke_launchers,
		self.line_marine_weaken_resolve,
		self.line_marine_word_of_emperer,
		self.line_marine_inquisition,
		self.line_marine_blessing_of_the_omnissiah]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)
#----------------база общих команд-----------------------
	
	def base_line_G_command(self):
		key = [
		"escape",
		"accept",
		"commandqueue",
		"systemmenu",
		"objectivesmenu",
		"alliesmenu",
		"chatmenu",
		"pause",
		"selectionfocus",
		"stop",
		"move",
		"attackmove",
		"attackmelee",
		"build",
		"buildadv",
		"attach",
		"attackground",
		"jump",
		"rally",
		"combatstance",
		"meleestance",
		"scuttle",
		"infiltrate",
		"unload",
		"deepstrike",
		"reinforce",
		"leader",
		"cancelconstruction",
		"rampage",
		"repair",
		"possess",
		"relocate",
		"cannibalism",
		"possess_enemy",
		"fear",
		"tau_snare_trap",
		"necron_solar_pulse",
		"tau_holographic_projection",
		"direct_spawn",
		"necron_stasis_field",
		"entrench",
		"burrow",
		"lightning_field",
		"direct_spawn_rally",
		"melee_dance",
		"harvest"]
		command = [
		self.line_escape,
		self.line_accept,
		self.line_commandqueue,
		self.line_systemmenu,
		self.line_objectivesmenu,
		self.line_alliesmenu,
		self.line_chatmenu,
		self.line_pause,
		self.line_selectionfocus,
		self.line_stop,
		self.line_move,
		self.line_attackmove,
		self.line_attackmelee,
		self.line_build,
		self.line_buildadv,
		self.line_attach,
		self.line_attackground,
		self.line_jump,
		self.line_rally,
		self.line_combatstance,
		self.line_meleestance,
		self.line_scuttle,
		self.line_infiltrate,
		self.line_unload,
		self.line_deepstrike,
		self.line_reinforce,
		self.line_leader,
		self.line_cancelconstruction,
		self.line_rampage,
		self.line_repair,
		self.line_possess,
		self.line_relocate,
		self.line_cannibalism,
		self.line_possess_enemy,
		self.line_fear,
		self.line_tau_snare_trap,
		self.line_necron_solar_pulse,
		self.line_tau_holographic_projection,
		self.line_direct_spawn,
		self.line_necron_stasis_field,
		self.line_entrench,
		self.line_burrow,
		self.line_lightning_field,
		self.line_direct_spawn_rally,
		self.line_melee_dance,
		self.line_harvest]

		def base_line_input(self):
			i = 0
			for i in range(len(command)):
				com =  command[i]
				word = key[i]
				i += 1
				Base_line.actual_line_show(self,com,word)
		base_line_input(self)

	def actual_line_show(self,com,word):
		Search_global.search_now(self,word)
		com.setText(a)
		
		
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()