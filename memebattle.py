import pgzrun, pygame, random, webbrowser
pygame.init()


WIDTH = 600 # Ширина окна
HEIGHT = 600 # Высота окна

TITLE = "Meme battle" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду

pch_time = 0
pch_time_pr = 0
pch_or = None

# Таймер
time1 = 0
real_time = 0
time1_r = 0
real_time_r = 0

couldown = 0
b_start = False
couldown2 = 0
sh_start = False
sh_v = False
sh2_v = False
couldown3 = 0
couldown4 = 0
boss1_attack_start1 = False
couldown5 = 0
sh2_start = False
r_start = True

couldown3_m = 0
couldown3_h = 0
couldown4_h = 0
couldown4_h = 0
boss1_attack_start1_m = False
boss1_attack_start_m = False
boss1_attack_start1_h = False
boss1_attack_start_h = False

couldown_2 = 0
couldown2_2 = 0
t_start = False
couldown_r = 0

difficulty = "Сложность: Лёгкая"
b_v = None
end_v = None

mode = "menu"
pause = False
music_reg = None

fon1 = Actor("fon1", (300, 300))
fon2 = Actor("fon2", (300, 300))
play = Actor("play", (300, 150))
cods = Actor("cods", (300, 250))
titles = Actor("titles", (300, 350))
floppa_menu = Actor("floppa_menu", (500, 500))
fakeMrBeast_menu = Actor("fakemrbeast_menu", (150, 480))
title = Actor("title", (300, 50))
cross = Actor("cross", (570, 30))
boss1 = Actor("fakemrbeast", (300, -50))
boss2 = Actor("bingus", (300, -50))
boss_ico1 = Actor("boss_ico", (300, 200))
boss_ico2 = Actor("boss_ico2_lock", (300, 450))
start = Actor("start", (300, 500))
start2 = Actor("start", (300, 350))
info_MrBeast = Actor("info_mrbeast", (300, 300))
info_Floppa = Actor("info_floppa", (300, 300))
coin = Actor("coin")
bitkoin = Actor("bitkoin")
pelmen = Actor("pelmen")
mega_tapok = Actor("mega_tapok")
shield = Actor("shield")
heart = Actor("heart")
warning = Actor("warning", (800, 250))
laser1 = Actor("laser1", (800, 300))
warning2 = Actor("warning", (800, 250))
laser2 = Actor("laser1", (800, 300))
warning3 = Actor("warning", (800, 250))
laser3 = Actor("laser1", (800, 300))
boss1_shield = Actor("boss1_shield", (0, 1000))
link2 = Actor("link_v", (300, 435))
brit = Actor("brit", (1600, 1000))
doska = Actor("doska", (300, 400))
volume = Actor("volume5", (300, 130))
arow_l = Actor("arow_left", (100, 130))
arow_r = Actor("arow_right", (500, 130))

volume1 = 1

rushes = []
wars = []
bullets = []
mega_bullets = []
bullets2 = []
mega_bullets2 = []
enemies2 = []
enemies = []
lasers = []


for i in range(7):
    x = random.randint(20, 580)
    y = random.randint(-100, -60)
    enemy = Actor("karl", (x, y))
    if difficulty == "Сложность: Лёгкая":
        enemy.speed = random.randint(3, 5)
    elif difficulty == "Сложность: Средняя":
        enemy.speed = random.randint(6, 8)
    elif difficulty == "Сложность: Сложная":
        enemy.speed = random.randint(9, 11)
    enemies.append(enemy)
for i in range(5):
    x= random.randint(20, 580)
    y = random.randint(-100, -60)
    enemy2 = Actor("sobaka", (x, y))
    if difficulty == "Сложность: Лёгкая":
        enemy2.speed = random.randint(3, 5)
    elif difficulty == "Сложность: Средняя":
        enemy2.speed = random.randint(6, 8)
    elif difficulty == "Сложность: Сложная":
        enemy2.speed = random.randint(9, 11)
    enemies2.append(enemy2)

player = Actor("mrbeast", (300, 550))

boss2_menu = False # По умолчанию False, True - открыть босс меню
man = False # По умолчанию False, True - открыть смену персов
timer = False
timer_1 = False
timer_boss1 = False
timer_boss2 = False
timer_boss1_m = False
timer_boss1_h = False
timer_r = False
timer_2 = False
boss1_attack_start = False
visual_timer = True
visual_timer_2 = True
person = "Текущий персонаж - MrBeast"
shield_health = 15
boss1_shield_health = 500
enemies_counter = 0
enemies_counter2 = 0
lvl = None
lvl2 = None
if difficulty == "Сложность: Лёгкая":
    boss1_hp = 3000
    boss2_hp = 2600
elif difficulty == "Сложность: Средняя":
    boss1_hp = 3200
    boss2_hp = 2800
elif difficulty == "Сложность: Сложная":
    boss1_hp = 3400
    boss2_hp = 3000

talk = 1
talk2 = 1

def draw():
    global mode, link2, music
    screen.fill("black")
    if mode == "menu":
        floppa_menu.draw()
        fakeMrBeast_menu.draw()
        play.draw()
        cods.draw()
        title.draw()
        titles.draw()
        screen.draw.text("Game by", center = (40, 590), color = "white", fontsize = 25)
        screen.draw.text("K4min", center = (110, 590), color = "red", fontsize = 25)
    elif mode == "cods":
        screen.draw.text("Громкость", center = (300, 60), color = "white", fontsize = 40)
        arow_l.draw()
        arow_r.draw()
        volume.draw()
        cross.draw()

    elif mode == "titles":
        cross.draw()
        screen.draw.text("Автор - K4minchik", center = (300, 100), color = "white", fontsize = 40)
        screen.draw.text("Код, спрайты, фоны - K4minchik", center = (300, 130), color = "white", fontsize = 35)

        screen.draw.text("Отдельное спасибо", center = (300, 200), color = "white", fontsize = 40)
        screen.draw.text(f"Kodland School, Учитель - Алиса Миронова", center = (300, 230), color = "white", fontsize = 35)

        screen.draw.text("Контакты", center = (300, 290), color = "white", fontsize = 40)
        screen.draw.text(f"Discord - K4min#7371\nEmail - orlovskayau17@gmail.com", center = (300, 325), color = "white", fontsize = 35)

        screen.draw.text("Поддержать автора", center = (300, 395), color = "white", fontsize = 40)
        link2.draw()
        link2.pos = (300, 450)
        screen.draw.text("Tincoff - 5536917761166435", center = (300, 425), color = "white", fontsize = 35)
        screen.draw.text("Version BETA 1.3", center = (300, 525), color = "white", fontsize = 35) # ВЕРСИЯ

    elif mode == "game":
        screen.draw.text("Выберите босса", center = (300, 50), color = "white", fontsize = 50)
        cross.draw()
        boss_ico1.draw()
        if boss2_menu == False:
            boss_ico2.draw()
        elif boss2_menu == True:
            boss_ico2.image = "boss_ico2"
            boss_ico2.draw()
        
        
    elif mode == "boss1_menu":
        screen.draw.text("Текущий босс - FAKE MrBeast", center = (300, 50), color = "white", fontsize = 40)
        if difficulty == "Сложность: Лёгкая":
            screen.draw.text(difficulty, center = (300, 120), color = "green", fontsize = 40)
        elif difficulty == "Сложность: Средняя":
            screen.draw.text(difficulty, center = (300, 120), color = "yellow", fontsize = 40)
        elif difficulty == "Сложность: Сложная":
            screen.draw.text(difficulty, center = (300, 120), color = "red", fontsize = 40)
        screen.draw.text("Менять - Space", center = (300, 160), color = "white", fontsize = 40)
        screen.draw.text(person, center = (300, 230), color = "white", fontsize = 40)
        screen.draw.text("Читать о персонаже - E", center = (300, 270), color = "white", fontsize = 40)
        if man == False:
            screen.draw.text("В данный момент нет других персонажей", center = (300, 340), color = "white", fontsize = 40)
        if man == True:
            screen.draw.text("Менять - X", center = (300, 340), color = "white", fontsize = 40)
        start.draw()
        cross.draw()

    elif mode == "boss2_menu":
        screen.draw.text("Текущий босс - Bingus", center = (300, 50), color = "white", fontsize = 40)
        if difficulty == "Сложность: Лёгкая":
            screen.draw.text(difficulty, center = (300, 120), color = "green", fontsize = 40)
        elif difficulty == "Сложность: Средняя":
            screen.draw.text(difficulty, center = (300, 120), color = "yellow", fontsize = 40)
        elif difficulty == "Сложность: Сложная":
            screen.draw.text(difficulty, center = (300, 120), color = "red", fontsize = 40)
        screen.draw.text("Менять - Space", center = (300, 160), color = "white", fontsize = 40)
        screen.draw.text(person, center = (300, 230), color = "white", fontsize = 40)
        screen.draw.text("Читать о персонаже - E", center = (300, 270), color = "white", fontsize = 40)
        if man == False:
            screen.draw.text("В данный момент нет других персонажей", center = (300, 340), color = "white", fontsize = 40)
        if man == True:
            screen.draw.text("Менять - X", center = (300, 340), color = "white", fontsize = 40)
        start.draw()
        cross.draw()
        
    elif mode == "info1":
        info_MrBeast.draw()
        screen.draw.text("Выйти - E", center = (510, 30), color = "white", fontsize = 40)
    elif mode == "info2":
        info_Floppa.draw()
        screen.draw.text("Выйти - E", center = (510, 30), color = "white", fontsize = 40)

    elif mode == "info":
        screen.draw.text("Управление", center = (300, 100), color = "white", fontsize = 60)
        screen.draw.text("Ходить - A/D \nУдар - ЛКМ \nСпособность - Space \nДоп. Способность - W\nПауза - ESC", center = (300, 200), color = "white", fontsize = 40)
        start2.draw()
    elif mode == "info_2":
        screen.draw.text("Управление", center = (300, 100), color = "white", fontsize = 60)
        screen.draw.text("Ходить - A/D \nУдар - ЛКМ \nСпособность - Space \nДоп. Способность - W\nПауза - ESC", center = (300, 200), color = "white", fontsize = 40)
        start2.draw()

        
    elif mode == "play1":
        fon1.draw()
        # Если персонаж == MrBeast
        if person == "Текущий персонаж - MrBeast":
            player.image = "mrbeast"
            # Отрисовка щита
            shield.draw()
            # Отрисовка пуль
            for i in range(len(bullets)):
                bullets[i].draw()
            for i in range(len(mega_bullets)):
                mega_bullets[i].draw()

            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown2 > 0 and sh_v == False:
                screen.draw.text(f"Доп. Способность через - {couldown2}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown2 <= 0 and sh_v == False:
                screen.draw.text("Доп. Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)
            elif sh_v == True:
                screen.draw.text("Доп. Способность через - Активация", center = (140, 30), color = "black", fontsize = 25)
                screen.draw.text(f"Здоровье щита - {shield_health}", center = (300, 330), color = "white", fontsize = 40)
        # Если персонаж == Floppa
        if person == "Текущий персонаж - Floppa":
            player.image = "floppa"
            # Отрисовка пуль
            for i in range(len(bullets2)):
                bullets2[i].draw()
            for i in range(len(mega_bullets2)):
                mega_bullets2[i].draw()
            for i in range(len(rushes)):
                rushes[i].draw()
            
            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown_r > 0:
                screen.draw.text(f"Доп. Способность через - {couldown_r}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown_r <= 0:
                screen.draw.text("Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)

        # Отрисовка врагов
        for i in range(len(enemies)):
            enemies[i].draw()   
        player.draw() # Персонаж/Игрок
        # Готовность
        if visual_timer == True:
            screen.draw.text("Приготовтесь", center = (300, 200), color = "black", fontsize = 40)
        elif visual_timer == False:
            screen.draw.text("", center = (300, 200), color = "black", fontsize = 40)
        
            

    elif mode == "play2":
        fon2.draw()
        # Если персонаж == MrBeast
        if person == "Текущий персонаж - MrBeast":
            player.image = "mrbeast"
            # Отрисовка щита
            shield.draw()
            # Отрисовка пуль
            for i in range(len(bullets)):
                bullets[i].draw()
            for i in range(len(mega_bullets)):
                mega_bullets[i].draw()

            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown2 > 0 and sh_v == False:
                screen.draw.text(f"Доп. Способность через - {couldown2}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown2 <= 0 and sh_v == False:
                screen.draw.text("Доп. Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)
            elif sh_v == True:
                screen.draw.text("Доп. Способность через - Активация", center = (120, 30), color = "black", fontsize = 25)
                screen.draw.text(f"Здоровье щита - {shield_health}", center = (300, 330), color = "white", fontsize = 40)
        # Если персонаж == Floppa
        if person == "Текущий персонаж - Floppa":
            player.image = "floppa"
            # Отрисовка пуль
            for i in range(len(bullets2)):
                bullets2[i].draw()
            for i in range(len(mega_bullets2)):
                mega_bullets2[i].draw()
            for i in range(len(rushes)):
                rushes[i].draw()
            
            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown_r > 0:
                screen.draw.text(f"Доп. Способность через - {couldown_r}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown_r <= 0:
                screen.draw.text("Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)

        # Отрисовка врагов
        for i in range(len(enemies2)):
            enemies2[i].draw()   
        player.draw() # Персонаж/Игрок
        # Готовность
        if visual_timer == True:
            screen.draw.text("Приготовтесь", center = (300, 200), color = "black", fontsize = 40)
        elif visual_timer == False:
            screen.draw.text("", center = (300, 200), color = "black", fontsize = 40)
    
    elif mode == "end":
        music1()
        player.image = "heart"
        player.draw()
        screen.draw.text("Game Over", center = (300, 200), color = "red", fontsize = 60)
        screen.draw.text("Нажмите R, чтобы начать заново", center = (300, 250), color = "white", fontsize = 40)
        screen.draw.text("Нажмите Q, чтобы вернуться в меню", center = (300, 290), color = "white", fontsize = 40)
        
    elif mode == "boss1":
        fon1.draw()
        player.draw()
        if talk == 1:
            screen.draw.text("Я MrBeast. Вопросы? \nДалее - Space", center = (300, 290), color = "black", fontsize = 40)
            boss1.draw()
        elif talk == 0:
            screen.draw.text("", center = (300, 290), color = "black", fontsize = 40)
            boss1.draw()
            if person == "Текущий персонаж - MrBeast":
                # Отрисовка пуль
                for i in range(len(bullets)):
                    bullets[i].draw()
                for i in range(len(mega_bullets)):
                    mega_bullets[i].draw()
                
                if couldown > 0:
                    screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
                elif couldown <= 0:
                    screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
                

            # Если персонаж == Floppa
            if person == "Текущий персонаж - Floppa":
                # Отрисовка пуль
                for i in range(len(bullets2)):
                    bullets2[i].draw()
                for i in range(len(mega_bullets2)):
                    mega_bullets2[i].draw()
                
                if couldown > 0:
                    screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
                elif couldown <= 0:
                    screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)

            # Отрисовка щита
            if sh2_v == True:
                boss1_shield.draw()
                screen.draw.text(f"Здоровье щита - {boss1_shield_health}", center = (300, 130), color = "white", fontsize = 40)
            laser1.draw()
            warning.draw()
            laser2.draw()
            warning2.draw()
            laser3.draw()
            warning3.draw()
            screen.draw.text(f"Жизни босса: {boss1_hp}", center = (480, 10), color = "black", fontsize = 25)

    elif mode == "boss2":
        fon2.draw()
        boss2.draw()
        player.draw()
        brit.draw()
        if talk2 == 1:
            screen.draw.text("Я жесткий диктатор.\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)
        elif talk2 == 2:
            screen.draw.text("Национал - \nкоммунистического государства.\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)    
        elif talk2 == 3:
            screen.draw.text("Все жители должны быть лысыми!\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)    
        elif talk2 == 4:
            screen.draw.text("Лысость - это гордость\nНАШЕГО ГОСУДАРСТВА! \nДалее - Space", center = (300, 300), color = "black", fontsize = 40)    
        elif talk2 == 0:
            screen.draw.text("", center = (300, 290), color = "black", fontsize = 40)
            boss2.draw()
            doska.draw()
            player.draw()
            if person == "Текущий персонаж - MrBeast":
                # Отрисовка пуль
                for i in range(len(bullets)):
                    bullets[i].draw()
                for i in range(len(mega_bullets)):
                    mega_bullets[i].draw()
                
                if couldown > 0:
                    screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
                elif couldown <= 0:
                    screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
                screen.draw.text("Вверх - W | Вниз - S", center = (120, 30), color = "black", fontsize = 25)
                

            # Если персонаж == Floppa
            if person == "Текущий персонаж - Floppa":
                # Отрисовка пуль
                for i in range(len(bullets2)):
                    bullets2[i].draw()
                for i in range(len(mega_bullets2)):
                    mega_bullets2[i].draw()
                
                if couldown > 0:
                    screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
                elif couldown <= 0:
                    screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)

            screen.draw.text(f"Жизни босса: {boss2_hp}", center = (480, 10), color = "black", fontsize = 25)

    elif mode == "win1":
        music1()
        fon1.draw()
        player.draw()
        boss1.draw()
        if talk == 2:
            screen.draw.text("Чёрт! \nДалее - Space", center = (300, 290), color = "black", fontsize = 40)
        elif talk == 3:
            screen.draw.text("Ладно, ты сильнее чем я думал. \nДалее - Space", center = (300, 290), color = "black", fontsize = 40)
        elif talk == 4:
            screen.draw.text("Я подпишу договор \nо продаже души\nДалее - Space", center = (300, 290), color = "black", fontsize = 40)
        elif talk == 5:
            screen.fill("black")
            screen.draw.text("Win", center = (300, 200), color = "green", fontsize = 60)
            screen.draw.text("Открыт новый босс - Bingus \n Открыт новый персонаж - Floppa", center = (300, 250), color = "white", fontsize = 40)
            screen.draw.text("Нажмите Space, чтобы продолжить", center = (300, 320), color = "white", fontsize = 40)

    elif mode == "win2":
        music1()
        fon2.draw()
        boss2.draw()
        player.draw()
        if talk2 == 5:
            screen.draw.text("Ауч!..\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)
        elif talk2 == 6:
            screen.draw.text("Ладно, ты не будешь лысым..\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)
        elif talk2 == 7:
            screen.draw.text("Забирай мою душу волосатик\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)
        elif talk2 == 8:
            screen.fill("black")
            screen.draw.text("Win", center = (300, 200), color = "green", fontsize = 60)
            screen.draw.text("Пожертвуй и я сделаю обнову :D", center = (300, 250), color = "white", fontsize = 40)
            screen.draw.text("Нажмите Space, чтобы продолжить", center = (300, 320), color = "white", fontsize = 40)

    elif mode == "pause1":
        fon1.draw()
        # Если персонаж == MrBeast
        if person == "Текущий персонаж - MrBeast":
            player.image = "mrbeast"
            # Отрисовка щита
            shield.draw()
            # Отрисовка пуль
            for i in range(len(bullets)):
                bullets[i].draw()
            for i in range(len(mega_bullets)):
                mega_bullets[i].draw()

            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown2 > 0 and sh_v == False:
                screen.draw.text(f"Доп. Способность через - {couldown2}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown2 <= 0 and sh_v == False:
                screen.draw.text("Доп. Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)
            elif sh_v == True:
                screen.draw.text("Доп. Способность через - Активация", center = (140, 30), color = "black", fontsize = 25)
                screen.draw.text(f"Здоровье щита - {shield_health}", center = (300, 330), color = "white", fontsize = 40)
        # Если персонаж == Floppa
        if person == "Текущий персонаж - Floppa":
            player.image = "floppa"
            # Отрисовка пуль
            for i in range(len(bullets2)):
                bullets2[i].draw()
            for i in range(len(mega_bullets2)):
                mega_bullets2[i].draw()
            for i in range(len(rushes)):
                rushes[i].draw()
            
            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown_r > 0:
                screen.draw.text(f"Доп. Способность через - {couldown_r}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown_r <= 0:
                screen.draw.text("Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)

        # Отрисовка врагов
        for i in range(len(enemies)):
            enemies[i].draw()   
        player.draw() # Персонаж/Игрок
        screen.draw.text("Пауза\nПродолжить - ESC", center = (300, 300), color = "black", fontsize = 60)

    elif mode == "pause2":
        fon2.draw()
        # Если персонаж == MrBeast
        if person == "Текущий персонаж - MrBeast":
            player.image = "mrbeast"
            # Отрисовка щита
            shield.draw()
            # Отрисовка пуль
            for i in range(len(bullets)):
                bullets[i].draw()
            for i in range(len(mega_bullets)):
                mega_bullets[i].draw()

            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown2 > 0 and sh_v == False:
                screen.draw.text(f"Доп. Способность через - {couldown2}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown2 <= 0 and sh_v == False:
                screen.draw.text("Доп. Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)
            elif sh_v == True:
                screen.draw.text("Доп. Способность через - Активация", center = (120, 30), color = "black", fontsize = 25)
                screen.draw.text(f"Здоровье щита - {shield_health}", center = (300, 330), color = "white", fontsize = 40)
        # Если персонаж == Floppa
        if person == "Текущий персонаж - Floppa":
            player.image = "floppa"
            # Отрисовка пуль
            for i in range(len(bullets2)):
                bullets2[i].draw()
            for i in range(len(mega_bullets2)):
                mega_bullets2[i].draw()
            for i in range(len(rushes)):
                rushes[i].draw()
            
            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
            if couldown_r > 0:
                screen.draw.text(f"Доп. Способность через - {couldown_r}", center = (140, 30), color = "black", fontsize = 25)
            elif couldown_r <= 0:
                screen.draw.text("Способность через - Готово", center = (140, 30), color = "black", fontsize = 25)

        # Отрисовка врагов
        for i in range(len(enemies2)):
            enemies2[i].draw()   
        player.draw() # Персонаж/Игрок
        screen.draw.text("Пауза\nПродолжить - ESC", center = (300, 300), color = "black", fontsize = 60)

    elif mode == "pause_boss1":
        fon1.draw()
        player.draw()
        screen.draw.text("", center = (300, 290), color = "black", fontsize = 40)
        boss1.draw()
        if person == "Текущий персонаж - MrBeast":
            # Отрисовка пуль
            for i in range(len(bullets)):
                bullets[i].draw()
            for i in range(len(mega_bullets)):
                mega_bullets[i].draw()
            
            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
                

        # Если персонаж == Floppa
        if person == "Текущий персонаж - Floppa":
            # Отрисовка пуль
            for i in range(len(bullets2)):
                bullets2[i].draw()
            for i in range(len(mega_bullets2)):
                mega_bullets2[i].draw()
                
            if couldown > 0:
                screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
            elif couldown <= 0:
                screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)

        # Отрисовка щита
        if sh2_v == True:
            boss1_shield.draw()
            screen.draw.text(f"Здоровье щита - {boss1_shield_health}", center = (300, 130), color = "white", fontsize = 40)
        laser1.draw()
        warning.draw()
        laser2.draw()
        warning2.draw()
        laser3.draw()
        warning3.draw()
        screen.draw.text(f"Жизни босса: {boss1_hp}", center = (480, 10), color = "black", fontsize = 25)
        screen.draw.text("Пауза\nПродолжить - ESC", center = (300, 300), color = "black", fontsize = 60)

    elif mode == "pause_boss2":
        fon2.draw()
        boss2.draw()
        player.draw()
        brit.draw()
        if talk2 == 1:
            screen.draw.text("Я жесткий диктатор.\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)
        elif talk2 == 2:
            screen.draw.text("Национал - \nкоммунистического государства.\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)    
        elif talk2 == 3:
            screen.draw.text("Все жители должны быть лысыми!\nДалее - Space", center = (300, 300), color = "black", fontsize = 40)    
        elif talk2 == 4:
            screen.draw.text("Лысость - это гордость\nНАШЕГО ГОСУДАРСТВА! \nДалее - Space", center = (300, 300), color = "black", fontsize = 40)    
        elif talk2 == 0:
            screen.draw.text("", center = (300, 290), color = "black", fontsize = 40)
            boss2.draw()
            doska.draw()
            player.draw()
            if person == "Текущий персонаж - MrBeast":
                # Отрисовка пуль
                for i in range(len(bullets)):
                    bullets[i].draw()
                for i in range(len(mega_bullets)):
                    mega_bullets[i].draw()
                
                if couldown > 0:
                    screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
                elif couldown <= 0:
                    screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)
                screen.draw.text("Вверх - W | Вниз - S", center = (120, 30), color = "black", fontsize = 25)
                

            # Если персонаж == Floppa
            if person == "Текущий персонаж - Floppa":
                # Отрисовка пуль
                for i in range(len(bullets2)):
                    bullets2[i].draw()
                for i in range(len(mega_bullets2)):
                    mega_bullets2[i].draw()
                
                if couldown > 0:
                    screen.draw.text(f"Способность через - {couldown}", center = (120, 10), color = "black", fontsize = 25)
                elif couldown <= 0:
                    screen.draw.text("Способность через - Готово", center = (120, 10), color = "black", fontsize = 25)

            screen.draw.text(f"Жизни босса: {boss2_hp}", center = (480, 10), color = "black", fontsize = 25)
            screen.draw.text("Пауза\nПродолжить - ESC", center = (300, 300), color = "black", fontsize = 60)

# Музыка
def music1():
    if mode == "play1":
        music.play("m2.mp3")
    elif mode == "play2":
        music.play("m3.mp3")
    elif mode == "end" or mode == "menu" or mode == "win1" or mode == "win2":
        music.stop()

# Ссылка
def link1(e = None): # !ОБРАТИТЕ ВНИМАНИЕ на e = None
        webbrowser.open("https://www.donationalerts.com/r/k4min")
 
# Перезапуск
def restart1():
    global timer, timer_1, sh2_start, real_time, visual_timer, sh2_v, pch_or, pch_time, pch_time_pr, talk, enemies_counter, lvl2, boss2_hp, timer_boss1, timer_boss2, boss1_hp, lvl, timer_boss1_h, timer_boss1_m, sh_v, enemies_counter2, timer_r, talk2, shield_health
    player.y = 550
    timer = True
    timer_1 = True
    timer_r = True
    sh_v = False
    sh2_v = False
    sh2_start = False
    visual_timer = True
    talk = 1
    talk2 = 1
    enemies_counter = 0
    enemies_counter2 = 0
    timer_boss1 = False
    timer_boss2 = False
    timer_boss1_m = False
    timer_boss1_h = False
    shield_health = 15
    brit.pos = (1600, 1000)
    lvl = None
    lvl2 = None
    laser1.x = 800
    warning.x = 800
    laser2.x = 800
    laser3.x = 800
    warning2.x = 800
    warning3.x = 800
    boss1.y = -50
    boss1_shield.y = 1000
    shield.y = 1000
    pch_time = 0
    pch_time_pr = 0
    pch_or = None

    for i in range(7):
        enemies.pop(i)
        new_enemy()
        enemies[i].y = -60
    for i in range(5):
        enemies2.pop(i)
        new_enemy2()
        enemies2[i].y = -60


def restart2():
    global timer, timer_1, visual_timer, timer_boss1, timer_boss2, timer_boss1_m, timer_boss1_h, sh_v
    player.y = 550
    sh_v = False
    timer = True
    timer_boss1 = True
    timer_boss2 = True
    timer_boss1_m = True
    timer_boss1_h = True

def restart3():
    global timer, timer_1, visual_timer, timer_boss1, timer_boss2, timer_boss1_m, timer_boss1_h, sh_v
    sh_v = False
    timer = True
    timer_boss1 = True
    timer_boss2 = True
    timer_boss1_m = True
    timer_boss1_h = True

# Сердце
def heart1():
    if mode == "end":
        animate(player, tween='linear', duration=1, x=300, y=350)
    if mode == "play1" or mode == "play2":
        player.y = 550
    if mode == "boss1" and talk == 1:
        animate(player, tween='linear', duration=1, x=300)
    if mode == "boss2" and talk2 == 1:
        animate(player, tween='linear', duration=1, x=300)
    if mode == "win1" and talk == 2:
        animate(player, tween='linear', duration=1, x=300)
    if mode == "win2" and talk2 == 5:
        animate(player, tween='linear', duration=1, x=300, y=550)

# Новый враг
def new_enemy():
    x = random.randint(20, 580)
    y = -60
    skin = random.randint(1, 2)
    if skin == 1:
        enemy = Actor("karl", (x, y))
    if skin == 2:
        enemy = Actor("chend", (x, y))
    if difficulty == "Сложность: Лёгкая":
        enemy.speed = random.randint(3, 5)
    elif difficulty == "Сложность: Средняя":
        enemy.speed = random.randint(6, 8)
    elif difficulty == "Сложность: Сложная":
        enemy.speed = random.randint(9, 11)
    enemies.append(enemy)

# Новый враг2
def new_enemy2():
    x = random.randint(20, 580)
    y = -60
    skin2 = random.randint(1, 2)
    if skin2 == 1:
        enemy2 = Actor("sobaka", (x, y))
    if skin2 == 2:
        enemy2 = Actor("sobaka2", (x, y))
    if difficulty == "Сложность: Лёгкая":
        enemy2.speed = random.randint(3, 5)
    elif difficulty == "Сложность: Средняя":
        enemy2.speed = random.randint(6, 8)
    elif difficulty == "Сложность: Сложная":
        enemy2.speed = random.randint(9, 11)
    enemies2.append(enemy2)
    
# Движение врагов
def enemy_ship():
    global visual_timer
    if real_time >= 1:
        visual_timer = False
        for i in range(len(enemies)):
            if enemies[i].y < 650:
                enemies[i].y += enemies[i].speed
            else:
                enemies.pop(i)
                new_enemy()

# Движение врагов
def enemy_ship2():
    global visual_timer
    if real_time >= 1:
        visual_timer = False
        for i in range(len(enemies2)):
            if enemies2[i].y < 650:
                enemies2[i].y += enemies2[i].speed
            else:
                enemies2.pop(i)
                new_enemy2()

# Столкновения
def collision():
    global mode, timer, real_time, time1, timer_1, shield_health, sh_v, enemies_counter, timer_r, boss2_hp, visual_timer, timer_boss1, boss1_hp, talk, lvl, boss1_shield_health, timer_boss2, sh2_v, enemies_counter2, end_v
    if mode == "play1":
        for i in range(len(enemies)):
            if player.colliderect(enemies[i]):
                mode = "end"
                end_v = 1
                timer = False
                timer_1 = False
                timer_r = False
            # MrBeast
            for j in range(len(bullets)):
                if bullets[j].colliderect(enemies[i]):
                    enemies.pop(i)
                    bullets.pop(j)
                    enemies_counter += 1
                    new_enemy()
                    break  
            for j in range(len(mega_bullets)):
                if mega_bullets[j].colliderect(enemies[i]):
                    enemies.pop(i)
                    enemies_counter += 1
                    new_enemy()
                    break
            for j in range(len(enemies)):
                if enemies[j].colliderect(shield):
                    enemies.pop(i)
                    shield_health -= 1
                    new_enemy()
                    break
            # Floppa
            for j in range(len(bullets2)):
                if bullets2[j].colliderect(enemies[i]):
                    enemies.pop(i)
                    bullets2.pop(j)
                    enemies_counter += 1
                    new_enemy()
                    break  
            for j in range(len(mega_bullets2)):
                if mega_bullets2[j].colliderect(enemies[i]):
                    enemies.pop(i)
                    enemies_counter += 1
                    new_enemy()
                    break
            for j in range(len(rushes)):
                if rushes[j].colliderect(enemies[i]):
                    enemies.pop(i)
                    enemies_counter += 1
                    new_enemy()
                    break

            if shield_health <= 0:
                timer_1 = True
                sh_v = False
                shield.y = 1000
                shield_health = 15

    if mode == "boss1":
        if player.colliderect(laser1):
            mode = "end"
            end_v = 1
            timer = False
            timer_1 = False
            timer_r = False
        if player.colliderect(laser2):
            mode = "end"
            end_v = 1
            timer = False
            timer_1 = False
            timer_r = False
        if player.colliderect(laser3):
            mode = "end"
            end_v = 1
            timer = False
            timer_1 = False
            timer_r = False
        # MrBeast
        for j in range(len(bullets)):
            if bullets[j].colliderect(boss1):
                boss1_hp -= 20
                bullets.pop(j)
                break 
        for j in range(len(mega_bullets)):
            if mega_bullets[j].colliderect(boss1):
                boss1_hp -= 2
                break

        for j in range(len(bullets)):
            if bullets[j].colliderect(boss1_shield):
                boss1_shield_health -= 20
                bullets.pop(j)
                break
        for j in range(len(mega_bullets)):
            if mega_bullets[j].colliderect(boss1_shield):
                boss1_shield_health -= 400
                mega_bullets.pop(j)
                break
        

        # Floppa
        for j in range(len(bullets2)):
            if bullets2[j].colliderect(boss1):
                boss1_hp -= 30
                bullets2.pop(j)
                break  
        for j in range(len(mega_bullets2)):
            if mega_bullets2[j].colliderect(boss1):
                boss1_hp -= 3
                break

        for j in range(len(bullets2)):
            if bullets2[j].colliderect(boss1_shield):
                boss1_shield_health -= 30
                bullets2.pop(j)
                break
        for j in range(len(mega_bullets2)):
            if mega_bullets2[j].colliderect(boss1_shield):
                boss1_shield_health -= 450
                mega_bullets2.pop(j)
                break

        if boss1_shield_health <= 0:
            sh2_v = False
            boss1_shield_health = 500
            boss1_shield.y = 1000


    if mode == "boss2":
        if player.colliderect(brit):
            mode = "end"
            end_v = 2
            timer = False
            timer_1 = False
            timer_r = False
        # MrBeast
        for j in range(len(bullets)):
            if bullets[j].colliderect(boss2):
                boss2_hp -= 20
                bullets.pop(j)
                break 
        for j in range(len(mega_bullets)):
            if mega_bullets[j].colliderect(boss2):
                boss2_hp -= 2
                break

        # Floppa
        for j in range(len(bullets2)):
            if bullets2[j].colliderect(boss2):
                boss2_hp -= 30
                bullets2.pop(j)
                break  
        for j in range(len(mega_bullets2)):
            if mega_bullets2[j].colliderect(boss2):
                boss2_hp -= 3
                break


    if mode == "play2":
        for i in range(len(enemies2)):
            if player.colliderect(enemies2[i]):
                mode = "end"
                end_v = 2
                timer = False
                timer_1 = False
                timer_r = False
            # MrBeast
            for j in range(len(bullets)):
                if bullets[j].colliderect(enemies2[i]):
                    enemies2.pop(i)
                    bullets.pop(j)
                    enemies_counter2 += 1
                    new_enemy2()
                    break  
            for j in range(len(mega_bullets)):
                if mega_bullets[j].colliderect(enemies2[i]):
                    enemies2.pop(i)
                    enemies_counter2 += 1
                    new_enemy2()
                    break
            for j in range(len(enemies2)):
                if enemies2[j].colliderect(shield):
                    enemies2.pop(i)
                    shield_health -= 1
                    new_enemy2()
                    break
            if shield_health <= 0:
                timer_1 = True
                sh_v = False
                shield.y = 1000
                shield_health = 15
            # Floppa
            for j in range(len(bullets2)):
                if bullets2[j].colliderect(enemies2[i]):
                    enemies2.pop(i)
                    bullets2.pop(j)
                    enemies_counter2 += 1
                    new_enemy2()
                    break  
            for j in range(len(mega_bullets2)):
                if mega_bullets2[j].colliderect(enemies2[i]):
                    enemies2.pop(i)
                    enemies_counter2 += 1
                    new_enemy2()
                    break
            for j in range(len(rushes)):
                if rushes[j].colliderect(enemies2[i]):
                    enemies2.pop(i)
                    enemies_counter2 += 1
                    new_enemy2()
                    break
            

# boss1
def timer1():
    if timer == True and pause == False:
        # Таймер
        global time1, real_time
        time1 += 1
        if time1 > 100:
            real_time = time1//100
    elif timer == False:
        time1 = 0
        real_time = 0 

def timer2():
    global time2, real_time2, couldown, b_start
    if timer == True and couldown > 0 and pause == False:
        # Таймер
        time2 += 1
        if time2 > 100:
            real_time2 = time2//100
        if real_time2 == 1:
            time2 = 0
            real_time2 = 0 
            couldown -= 1
        if couldown <= 0:
            b_start = True
        elif couldown > 0:
            b_start = False
    elif timer == False:
        time2 = 0
        real_time2 = 0   
        couldown = 3

def timer1_r():
    if timer_r == True and pause == False:
        # Таймер
        global time1_r, real_time_r
        time1_r += 1
        if time1_r > 100:
            real_time_r = time1_r//100
    elif timer_r == False:
        time1_r = 0
        real_time_r = 0 

def timer2_r():
    global time2_r, real_time2_r, couldown_r, r_start
    if timer_r == True and couldown_r > 0 and pause == False:
        # Таймер
        time2_r += 1
        if time2_r > 100:
            real_time2_r = time2_r//100
        if real_time2_r == 1:
            time2_r = 0
            real_time2_r = 0 
            couldown_r -= 1
        if couldown_r <= 0:
            r_start = True
        elif couldown_r > 0:
            r_start = False
    elif timer_r == False:
        time2_r = 0
        real_time2_r = 0   
        couldown_r = 3

def timer3():
    global time3, real_time3, couldown2, sh_start, timer_1
    if timer_1 == True and couldown2 > 0 and pause == False:
        # Таймер
        time3 += 1
        if time3 > 100:
            real_time3 = time3//100
        if real_time3 == 1:
            time3 = 0
            real_time3 = 0 
            couldown2 -= 1
        if couldown2 <= 0:
            sh_start = True
        elif couldown2 > 0:
            sh_start = False
    elif timer_1 == False:
        time3 = 0
        real_time3 = 0   
        couldown2 = 3

def timer_boss_1():
    global time4, real_time4, couldown, boss1_attack_start, boss1_attack_start1, couldown3, couldown4
    if timer_boss1 == True and couldown3 > 0 and pause == False:
        # Таймер
        time4 += 1
        if time4 > 100:
            real_time4 = time4//100
        if real_time4 == 1:
            time4 = 0
            real_time4 = 0 
            couldown3 -= 1
            if boss1_attack_start == True:
                couldown4 -= 1
        if couldown3 <= 0:
            boss1_attack_start = True
        elif couldown3 > 0:
            boss1_attack_start = False
        if couldown4 <= 0:
            boss1_attack_start1 = True
        elif couldown4 > -2:
            boss1_attack_start1 = False  
    elif timer_boss1 == False:
        time4 = 0
        real_time4 = 0   
        couldown3 = 2
        couldown4 = 1

def timer_boss_1_m():
    global time4_m, real_time4_m, boss1_attack_start_m, boss1_attack_start1_m, couldown3_m, couldown4_m
    if timer_boss1_m == True and couldown3_m > 0 and pause == False:
        # Таймер
        time4_m += 1
        if time4_m > 100:
            real_time4_m = time4_m//100
        if real_time4_m == 1:
            time4_m = 0
            real_time4_m = 0 
            couldown3_m -= 1
            if boss1_attack_start_m == True:
                couldown4_m -= 1
        if couldown3_m <= 0:
            boss1_attack_start_m = True
        elif couldown3_m > 0:
            boss1_attack_start_m = False
        if couldown4_m <= 0:
            boss1_attack_start1_m = True
        elif couldown4_m > -2:
            boss1_attack_start1_m = False  
    elif timer_boss1_m == False:
        time4_m = 0
        real_time4_m = 0   
        couldown3_m = 2
        couldown4_m = 1

def timer_boss_1_h():
    global time4_h, real_time4_h, boss1_attack_start_h, boss1_attack_start1_h, couldown3_h, couldown4_h
    if timer_boss1_h == True and couldown3_h > 0 and pause == False:
        # Таймер
        time4_h += 1
        if time4_h > 100:
            real_time4_h = time4_h//100
        if real_time4_h == 1:
            time4_h = 0
            real_time4_h = 0 
            couldown3_h -= 1
            if boss1_attack_start_h == True:
                couldown4_h -= 1
        if couldown3_h <= 0:
            boss1_attack_start_h = True
        elif couldown3_h > 0:
            boss1_attack_start_h = False
        if couldown4_h <= 0:
            boss1_attack_start1_h = True
        elif couldown4_h > -2:
            boss1_attack_start1_h = False  
    elif timer_boss1_h == False:
        time4_h = 0
        real_time4_h = 0   
        couldown3_h = 2
        couldown4_h = 1

def timer_boss_2():
    global time5, real_time5, couldown5, sh2_start, timer_boss2, boss1_shield_health
    if timer_boss2 == True and couldown5 > 0 and pause == False:
        # Таймер
        time5 += 1
        if time5 > 100:
            real_time5 = time5//100
        if real_time5 == 1:
            time5 = 0
            real_time5 = 0 
            couldown5 -= 1
        if couldown5 <= 0:
            sh2_start = True
        elif couldown5 > 0:
            sh2_start = False
    elif timer_boss2 == False:
        time5 = 0
        real_time5 = 0   
        couldown5 = 5


def boss_fight1():
    global mode, talk, lvl, boss1_hp, pch_or, pch_time_pr
    if enemies_counter >= 150 and difficulty == "Сложность: Лёгкая":
        if talk == 1:
            mode = "boss1"
            animate(boss1, tween='linear', duration=0.5, y = 100)
            boss1_hp = 6000
        elif talk == 0:
            lvl = 1
        if boss1_hp <= 0 and mode == "boss1":
            talk = 2
            mode = "win1"
    if enemies_counter >= 200 and difficulty == "Сложность: Средняя":
        if talk == 1:
            mode = "boss1"
            animate(boss1, tween='linear', duration=0.5, y = 100)
            boss1_hp = 7000
        elif talk == 0:
            lvl = 1
        if boss1_hp <= 0 and mode == "boss1":
            talk = 2
            mode = "win1"
    if enemies_counter >= 300 and difficulty == "Сложность: Сложная":
        if talk == 1:
            mode = "boss1"
            animate(boss1, tween='linear', duration=0.5, y = 100)
            boss1_hp = 8000
        elif talk == 0:
            lvl = 1
        if boss1_hp <= 0 and mode == "boss1":
            talk = 2
            mode = "win1"
        
        
            

def lvl1():
    if lvl == 1:
        global timer, timer_1, couldown3, random_laser, random_laser2, random_laser3, warning, timer_r, laser1, laser2, laser3, warning2, warning3, sh_v, sh2_v, couldown2, boss1_shield, timer_boss2, boss1_shield_health, couldown5, couldown3_h, couldown3_m
        timer = False
        timer_1 = False
        timer_r = False
        restart2()
        if difficulty == "Сложность: Лёгкая" or difficulty == "Сложность: Средняя" or difficulty == "Сложность: Сложная":
            if mode == "boss1" and boss1_attack_start == True:
                laser1.x = 800
                random_laser = random.randint(60, 540)
                warning = Actor("warning")
                warning.x = random_laser
                warning.y = 250
                couldown3 = 2
            if mode == "boss1" and couldown3 == 1:
                laser1.x = warning.x
            if mode == "boss1" and boss1_attack_start1 == True:
                warning.x = 800

        if difficulty == "Сложность: Средняя" or difficulty == "Сложность: Сложная":
            if mode == "boss1" and boss1_attack_start_m == True:
                laser2.x = 800
                random_laser2 = random.randint(60, 540)
                warning2 = Actor("warning")
                warning2.x = random_laser2
                warning2.y = 250
                couldown3_m = 2
            if mode == "boss1" and couldown3_m == 1:
                laser2.x = warning2.x
            if mode == "boss1" and boss1_attack_start1_m == True:
                warning2.x = 800

        if difficulty == "Сложность: Сложная":
            if mode == "boss1" and boss1_attack_start_h == True:
                laser3.x = 800
                random_laser3 = random.randint(60, 540)
                warning3 = Actor("warning")
                warning3.x = random_laser3
                warning3.y = 250
                couldown3_h = 2
            if mode == "boss1" and couldown3_h == 1:
                laser3.x = warning.x
            if mode == "boss1" and boss1_attack_start1_h == True:
                warning3.x = 800

        if mode == "boss1" and sh2_start == True:
            boss1_shield = Actor("boss1_shield", (300, 1000))
            boss1_shield.y = 100
            sh2_v = True
            couldown5 = 5

def boss_fight2():
    global mode, talk2, lvl2, boss2_hp, pch_or, pch_time_pr
    if enemies_counter2 >= 150 and difficulty == "Сложность: Лёгкая":
        if talk2 == 1:
            mode = "boss2"
            animate(boss2, tween='linear', duration=2, y = 150)
            boss2_hp = 4000
        elif talk2 == 0:
            lvl2 = 1
        if boss2_hp <= 0 and mode == "boss2":
            talk2 = 5
            mode = "win2"
    if enemies_counter2 >= 200 and difficulty == "Сложность: Средняя":
        if talk2 == 1:
            mode = "boss2"
            animate(boss2, tween='linear', duration=2, y = 150)
            boss2_hp = 5000
        elif talk2 == 0:
            lvl2 = 1
        if boss2_hp <= 0 and mode == "boss2":
            talk2 = 5
            mode = "win2"
    if enemies_counter2 >= 300 and difficulty == "Сложность: Сложная":
        if talk2 == 1:
            mode = "boss2"
            animate(boss2, tween='linear', duration=2, y = 150)
            boss2_hp = 6000
        elif talk2 == 0:
            lvl2 = 1
        if boss2_hp <= 0 and mode == "boss2":
            talk2 = 5
            mode = "win2"



def lvl_2():
    if lvl2 == 1:
        global timer, timer_1, couldown3, random_laser, random_laser2, random_laser3, warning, timer_r, laser1, laser2, laser3, warning2, warning3, y2, sh_v, sh2_v, couldown2, boss1_shield, timer_boss2, boss1_shield_health, couldown5, couldown3_h, couldown3_m
        timer = False
        timer_1 = False
        timer_r = False
        restart3()
        if difficulty == "Сложность: Лёгкая":
            if pause == False:
                # Движение бритвы
                if brit.x > -250:
                    brit.x -= 5
                else:
                    brit.x = 1500
                    y2 = random.randint(1,2)
                    if y2 == 1:
                        brit.y = 500
                    elif y2 == 2:
                        brit.y = 300

        if difficulty == "Сложность: Средняя":
            if pause == False:
                # Движение бритвы
                if brit.x > -250:
                    brit.x -= 10
                else:
                    brit.x = 1500
                    y2 = random.randint(1,2)
                    if y2 == 1:
                        brit.y = 500
                    elif y2 == 2:
                        brit.y = 300

        if difficulty == "Сложность: Сложная":
            if pause == False:
                # Движение бритвы
                if brit.x > -250:
                    brit.x -= 15
                else:
                    brit.x = 1500
                    y2 = random.randint(1,2)
                    if y2 == 1:
                        brit.y = 500
                    elif y2 == 2:
                        brit.y = 300


            
# Update         
def update(dt):
    global mode, couldown_2
    lvl1()
    lvl_2()
    heart1()
    boss_fight1()
    boss_fight2()
    timer1()
    timer2()
    timer3()
    timer1_r()
    timer2_r()
    timer_boss_1()
    timer_boss_2()
    timer_boss_1_m()
    timer_boss_1_h()
    if mode == "play1":
        enemy_ship()
    if mode == "play2":
        enemy_ship2()
    collision()
    #Управление
    if keyboard.A and player.x > 0 and mode == "play1" or keyboard.A and player.x > 0 and mode == "boss1" and lvl == 1:
        player.x -= 7
    elif keyboard.D and player.x < WIDTH and mode == "play1" or keyboard.D and player.x < WIDTH and mode == "boss1" and lvl == 1:
        player.x += 7
    #Управление
    if keyboard.A and player.x > 0 and mode == "play2" or keyboard.A and player.x > 0 and mode == "boss2" and lvl2 == 1:
        player.x -= 7
    elif keyboard.D and player.x < WIDTH and mode == "play2" or keyboard.D and player.x < WIDTH and mode == "boss2" and lvl2 == 1:
        player.x += 7


    if pause == False:
        # Движение пули 
        for i in range(len(bullets)):
            if bullets[i].y < -20:
                bullets.pop(i)
                break
            else:
                bullets[i].y -= 10
        for i in range(len(mega_bullets)):
            if mega_bullets[i].y < -20:
                mega_bullets.pop(i)
                break
            else:
                mega_bullets[i].y -= 10

        # Движение пули 2
        for i in range(len(bullets2)):
            if bullets2[i].y < -20:
                bullets2.pop(i)
                break
            else:
                bullets2[i].y -= 10

        for i in range(len(mega_bullets2)):
            if mega_bullets2[i].y < -20:
                mega_bullets2.pop(i)
                break
            else:
                mega_bullets2[i].y -= 10
                mega_bullets2[i].angle += 10

        for i in range(len(rushes)):
            if rushes[i].y < -20:
                rushes.pop(i)
                break
            else:
                rushes[i].x -= 50


    # Движение босса
    global pch_time, pch_time_pr, pch_or
    if pch_time_pr == 1:
        pch_time += 1
    if pch_time >= 1 * FPS:
        if pch_or == 'up':
            animate(boss1, y = boss1.y - 10, duration = 1, tween="accel_decel")
            animate(boss2, y = boss2.y - 10, duration = 1, tween="accel_decel")
            pch_time = 0
            pch_or = 'down'
        elif pch_or == 'down':
            animate(boss1, y = boss1.y + 10, duration = 1, tween="accel_decel")
            animate(boss2, y = boss2.y + 10, duration = 1, tween="accel_decel")
            pch_time = 0
            pch_or = 'up'
        
        
def on_mouse_down(button, pos):
    global mode, visual_timer, real_time, time1, timer_1, volume1
    if button == mouse.LEFT and mode == "menu":
        if cods.collidepoint(pos):
            mode = "cods"
        if play.collidepoint(pos):
            mode = "game"
        if titles.collidepoint(pos):
            mode = "titles"
    elif button == mouse.LEFT and mode == "titles":
        if cross.collidepoint(pos):
            mode = "menu"
        elif link2.collidepoint(pos):
            link1()
    elif button == mouse.LEFT and mode == "cods":
        if cross.collidepoint(pos):
            mode = "menu"
        elif arow_l.collidepoint(pos) and volume1 == 1:
            music.set_volume(0.75)
            volume.image = "volume4"
            volume1 = 0.75
        elif arow_l.collidepoint(pos) and volume1 == 0.75:
            music.set_volume(0.5)
            volume.image = "volume3"
            volume1 = 0.5
        elif arow_l.collidepoint(pos) and volume1 == 0.5:
            music.set_volume(0.25)
            volume.image = "volume2"
            volume1 = 0.25
        elif arow_l.collidepoint(pos) and volume1 == 0.25:
            music.set_volume(0)
            volume.image = "volume1"
            volume1 = 0
        elif arow_r.collidepoint(pos) and volume1 == 0:
            music.set_volume(0.25)
            volume.image = "volume2"
            volume1 = 0.25
        elif arow_r.collidepoint(pos) and volume1 == 0.25:
            music.set_volume(0.5)
            volume.image = "volume3"
            volume1 = 0.5
        elif arow_r.collidepoint(pos) and volume1 == 0.5:
            music.set_volume(0.75)
            volume.image = "volume4"
            volume1 = 0.75
        elif arow_r.collidepoint(pos) and volume1 == 0.75:
            music.set_volume(1)
            volume.image = "volume5"
            volume1 = 1
    elif button == mouse.LEFT and mode == "game":
        if cross.collidepoint(pos):
            mode = "menu"
        elif boss_ico1.collidepoint(pos):
            mode = "boss1_menu"
        elif boss_ico2.collidepoint(pos) and boss2_menu == True:
            mode = "boss2_menu"
    elif button == mouse.LEFT and mode == "boss1_menu":
        if cross.collidepoint(pos):
            mode = "game"
        elif start.collidepoint(pos):
            mode = "info"
    elif button == mouse.LEFT and mode == "boss2_menu":
        if cross.collidepoint(pos):
            mode = "game"
        elif start.collidepoint(pos):
            mode = "info_2"
    elif button == mouse.LEFT and mode == "info":
        global timer
        if start2.collidepoint(pos):
            mode = "play1"
            restart1()
            music1()
    elif button == mouse.LEFT and mode == "info_2":
        global timer_2
        if start2.collidepoint(pos):
            mode = "play2"
            restart1()
            music1()
    elif button == mouse.LEFT and mode == "play1" and person == "Текущий персонаж - MrBeast" or button == mouse.LEFT and mode == "boss1" and person == "Текущий персонаж - MrBeast" or button == mouse.LEFT and mode == "play2" and person == "Текущий персонаж - MrBeast" or button == mouse.LEFT and mode == "boss2" and person == "Текущий персонаж - MrBeast":
        bullet = Actor("coin")
        bullet.pos = player.pos
        bullets.append(bullet)
    elif button == mouse.LEFT and mode == "play1" and person == "Текущий персонаж - Floppa" or button == mouse.LEFT and mode == "boss1" and person == "Текущий персонаж - Floppa" or button == mouse.LEFT and mode == "play2" and person == "Текущий персонаж - Floppa" or button == mouse.LEFT and mode == "boss2" and person == "Текущий персонаж - Floppa":
        bullet2 = Actor("pelmen")
        bullet2.pos = player.pos
        bullets2.append(bullet2)

def on_key_down(key):
    global time1, timer, real_time, couldown, couldown2, timer_1, sh_v, talk, boss2_menu, man, shield, b_v, couldown_2, pch_time, pch_time_pr, pch_or, couldown_r, talk2, player, pause
    global mode, visual_timer
    global difficulty
    global person
    # Boss1 Menu
    # Смена сложности
    if keyboard.space and mode == "boss1_menu" and difficulty == "Сложность: Лёгкая":
        difficulty = "Сложность: Средняя"
    elif keyboard.space and mode == "boss1_menu" and difficulty == "Сложность: Средняя":
        difficulty = "Сложность: Сложная"
    elif keyboard.space and mode == "boss1_menu" and difficulty == "Сложность: Сложная":
        difficulty = "Сложность: Лёгкая"
    # Выбор персонажа
    if keyboard.X and man == True and person == "Текущий персонаж - MrBeast" and mode == "boss1_menu":
        person = "Текущий персонаж - Floppa"
    elif keyboard.X and man == True and person == "Текущий персонаж - Floppa" and mode == "boss1_menu":
        person = "Текущий персонаж - MrBeast"
    # Информация о персонаже
    if keyboard.E and mode == "boss1_menu" and person == "Текущий персонаж - MrBeast":
        mode = "info1"
        b_v = 1
    elif keyboard.E and mode == "boss1_menu" and person == "Текущий персонаж - Floppa":
        mode = "info2"
        b_v = 1
    elif keyboard.E and mode == "info1" and b_v == 1 or keyboard.E and mode == "info2" and b_v == 1:
        mode = "boss1_menu"
    # Перезапуск
    if mode == "end" and keyboard.Q:
        mode = "menu"
        music1()
    elif mode == "end" and keyboard.R:
        restart1()
        if end_v == 1:
            mode = "play1"
        elif end_v == 2:
            mode = "play2"
        music1()
    
    # Пауза
    if mode == "play1" and keyboard.ESCAPE and visual_timer == False:
        mode = "pause1"
        pause = True
        music.pause()
    elif mode == "pause1":
        mode = "play1"
        pause = False
        music.unpause()

    if mode == "play2" and keyboard.ESCAPE and visual_timer == False:
        mode = "pause2"
        pause = True
        music.pause()
    elif mode == "pause2":
        mode = "play2"
        pause = False
        music.unpause()

    if mode == "boss1" and keyboard.ESCAPE and talk == 0:
        mode = "pause_boss1"
        pause = True
        music.pause()
    elif mode == "pause_boss1":
        mode = "boss1"
        pause = False
        music.unpause()
        
    if mode == "boss2" and keyboard.ESCAPE and talk2 == 0:
        mode = "pause_boss2"
        pause = True
        music.pause()
    elif mode == "pause_boss2":
        mode = "boss2"
        pause = False
        music.unpause()
        

        

    # Запуск Способности mrbeast
    if mode == "play1" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - MrBeast" or mode == "boss1" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - MrBeast":
        if talk == 0 or talk2 == 0 or mode == "play1":
            mega_bullet = Actor("bitkoin")
            mega_bullet.pos = player.pos
            mega_bullets.append(mega_bullet)
            couldown = 3
    # Запуск Доп. Способности mrbeast
    if mode == "play1" and keyboard.W and sh_start == True and person == "Текущий персонаж - MrBeast":
        shield = Actor("shield", (300, 500))
        #timer_1 = False
        sh_v = True
        couldown2 = 3
    # Запуск Способности floppa
    if mode == "play1" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - Floppa" or mode == "boss1" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - Floppa":
        if talk == 0 or talk2 == 0 or mode == "play1":
            mega_bullet2 = Actor("mega_tapok")
            mega_bullet2.pos = player.pos
            mega_bullets2.append(mega_bullet2)
            couldown = 3
    # Запуск Доп. Способности floppa
    if mode == "play1" and keyboard.W and r_start == True and person == "Текущий персонаж - Floppa" or mode == "boss1" and keyboard.W and r_start == True and person == "Текущий персонаж - Floppa":
        rush = Actor("kega")
        rush.pos = (900, 400)
        rushes.append(rush)
        couldown_r = 3

    # Диалог
    if mode == "boss1" and keyboard.SPACE and talk == 1:
        music1()
        boss1.y = 100
        talk = 0
        pch_time_pr = 1
        pch_or = 'up'
    elif mode == "win1" and keyboard.SPACE and talk == 2:
        talk = 3
    elif mode == "win1" and keyboard.SPACE and talk == 3:
        talk = 4
    elif mode == "win1" and keyboard.SPACE and talk == 4:
        talk = 5
    elif mode == "win1" and keyboard.SPACE and talk == 5:
        mode = "menu"
        man = True
        boss2_menu = True

    # Диалог2
    if mode == "boss2" and keyboard.SPACE and talk2 == 1:
        talk2 = 2
    elif mode == "boss2" and keyboard.SPACE and talk2 == 2:
        talk2 = 3
    elif mode == "boss2" and keyboard.SPACE and talk2 == 3:
        talk2 = 4
    elif mode == "boss2" and keyboard.SPACE and talk2 == 4:
        music1()
        boss2.y = 150
        talk2 = 0
        pch_time_pr = 1
        pch_or = 'up'
    if mode == "win2" and keyboard.SPACE and talk2 == 5:
        talk2 = 6
    elif mode == "win2" and keyboard.SPACE and talk2 == 6:
        talk2 = 7
    elif mode == "win2" and keyboard.SPACE and talk2 == 7:
        talk2 = 8
    elif mode == "win2" and keyboard.SPACE and talk2 == 8:
        mode = "menu"



    # Boss2 Menu
    # Смена сложности
    if keyboard.space and mode == "boss2_menu" and difficulty == "Сложность: Лёгкая":
        difficulty = "Сложность: Средняя"
    elif keyboard.space and mode == "boss2_menu" and difficulty == "Сложность: Средняя":
        difficulty = "Сложность: Сложная"
    elif keyboard.space and mode == "boss2_menu" and difficulty == "Сложность: Сложная":
        difficulty = "Сложность: Лёгкая"
    # Выбор персонажа
    if keyboard.X and man == True and person == "Текущий персонаж - MrBeast" and mode == "boss2_menu":
        person = "Текущий персонаж - Floppa"
    elif keyboard.X and man == True and person == "Текущий персонаж - Floppa" and mode == "boss2_menu":
        person = "Текущий персонаж - MrBeast"
    # Информация о персонаже
    if keyboard.E and mode == "boss2_menu" and person == "Текущий персонаж - MrBeast":
        mode = "info1"
        b_v = 2
    elif keyboard.E and mode == "boss2_menu" and person == "Текущий персонаж - Floppa":
        mode = "info2"
        b_v = 2
    elif keyboard.E and mode == "info2" and b_v == 2 or keyboard.E and mode == "info1" and b_v == 2:
        mode = "boss2_menu"

    # Запуск Способности mrbeastd
    if mode == "play2" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - MrBeast" or mode == "boss2" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - MrBeast":
        if talk == 0 or talk2 == 0 or mode == "play2":
            mega_bullet = Actor("bitkoin")
            mega_bullet.pos = player.pos
            mega_bullets.append(mega_bullet)
            couldown = 3
    # Запуск Доп. Способности mrbeast
    if mode == "play2" and keyboard.W and sh_start == True and person == "Текущий персонаж - MrBeast":
        shield = Actor("shield", (300, 500))
        sh_v = True
        couldown2 = 3
    # Запуск Способности floppa
    if mode == "play2" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - Floppa" or mode == "boss2" and keyboard.SPACE and b_start == True and person == "Текущий персонаж - Floppa":
        if talk == 0 or talk2 == 0 or mode == "play2":
            mega_bullet2 = Actor("mega_tapok")
            mega_bullet2.pos = player.pos
            mega_bullets2.append(mega_bullet2)
            couldown = 3
    # Запуск Доп. Способности floppa
    if mode == "play2" and keyboard.W and r_start == True and person == "Текущий персонаж - Floppa":
        rush = Actor("kega")
        rush.pos = (900, 400)
        rushes.append(rush)
        couldown_r = 3
    
    # Для боссфайта2
    if keyboard.W and mode == "boss2" and lvl2 == 1 and player.y == 550:
        animate(player, tween='linear', duration=0.2, y=320)
    elif keyboard.S and mode == "boss2" and lvl2 == 1 and player.y == 320:
        animate(player, tween='linear', duration=0.2, y=550)
pgzrun.go()
