import pygame
from PIL import Image
import time
import random
while True:
   password = input("请输入八位密码：") 
   if password == "20190323":
      image = Image.open("my_image.jpg")
      image.show()
      break
   else:
      print("密码错误！再想想吧。")


while True:
    password2 = input("请输入新的密码加上你写给我的第一封信：")  
    if password2 == "20220320Nothing":  # 如果密码正确
        print("正确！多亏了显显的勇敢，虽然曲折，但是我们的故事就此开始。")
        break  
    else:
        print("再想想吧。你写给我的第一封信叫什么名字呢？（大写首字母！）")

print("时间来到2019年的四月，马小姐第一次收到来自黄先生的投喂。黄先生还记得是什么吗？")

while True:
    password3 = input("虽然并非是那一次你说的话，但请喊出黄先生投喂马小姐的名言：\n""——！——————，——！：")
    if password3 == "吃！马小姐，吃！":
       image = Image.open("image2.png")
       image.show()
       print("是这几个很好吃的蛋糕哦~")
       break
    else:
        print("再想想吧。你写在便签上的名言。")

while True:
   password4 = input("炎热的五月，在黄先生的私人家教下，马小姐的微积分拿到了：")
   if password4 == "5":
      image = Image.open("image3.png")
      image.show()
      print("答对啦！奖励你我们各种意义上的第一张合照！还记得我们站在哪里吗？")
      break
   else:
      print("不会吧不会吧？这可是你的教学成果哦？")

print("2019年7月12日，是黄先生离开的日子。我本以为我们就该就此结束。")
print("但是我们留给彼此的烙印实在太多太多。\n 看来，我们俩都不想放手呢！\n两个小孩开始学着怎么让自己的温柔越过茫茫的太平洋，落在彼此身上")

while True:
   password5 = input("提问！马小姐给黄先生的践行礼物上用金色的墨水题字：")
   if password5 == "NKISC黄显":
      image = Image.open("image4.png")
      image.show()
      print("这些就是我们在那段日子里努力的证明。")
      break
   else:
      print("这个答案里没有空格哦？如果实在想不起来，找一找照片吧？")

print("2019年7月12日。我们再度重逢。\n两个小孩觉得这几个月是那样的漫长，以至于再见都会热泪盈眶。")
for i in range(2):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("在阴冷的冬天，马小姐知道会有一个穿着一节一节羽绒服的身影，\n风雨无阻地在校门等待着她。\n她一下课就会想起那双暖呼呼的柔软的手\n也许还带着点好吃的\n一路把她送回家")
for i in range(2):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("接下来就是我们跨的第一个年。在成都暖黄色的灯光里，我们沦陷在彼此温暖的拥抱里。\n某个便利店小哥：现在的年轻人啊。。")
for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("可明明是那么相爱的两个人，却一定要分离。")

pygame.init()


window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))


block_size = 50
block1_x = 50
block1_y = 200
block2_x = 400
block2_y = 200


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.draw.rect(window, (255, 0, 0), (block1_x, block1_y, block_size, block_size))
    pygame.draw.rect(window, (0, 0, 255), (block2_x, block2_y, block_size, block_size))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        block1_y -= 5
    elif keys[pygame.K_DOWN]:
        block1_y += 5
    elif keys[pygame.K_LEFT]:
        block1_x -= 5
    elif keys[pygame.K_RIGHT]:
        block1_x += 5

    
    if block1_x + block_size > block2_x and block1_x < block2_x + block_size and block1_y + block_size > block2_y and block1_y < block2_y + block_size:
        print("恭喜你，你的思念触摸到了马小姐")
        running = False

    
    pygame.display.flip()


pygame.quit()

print("就是这样，在我们耐心，信任，思念和爱意下，太平洋的鸿沟不过是你微笑的唇角。")

for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)

print("那么，缺少着拥抱和亲吻，我们爱又是怎么样的呢？")
for i in range(2):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('爱是信任与跟随')


red_rect_x = 50
red_rect_y = 250
red_rect_speed = 0


green_rect_x = 100
green_rect_y = 250
green_rect_speed = 0


rect_size = 50
red_color = (255, 0, 0)
green_color = (0, 255, 0)


end_rect_x = screen_width - rect_size
end_rect_y = screen_height // 2 - rect_size // 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                red_rect_speed = -1
            elif event.key == pygame.K_DOWN:
                red_rect_speed = 1
            elif event.key == pygame.K_LEFT:
                red_rect_x -= 30
            elif event.key == pygame.K_RIGHT:
                red_rect_x += 30

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                red_rect_speed = 0

    
    red_rect_y += red_rect_speed

    
    if red_rect_y < 0:
        red_rect_y = 0
    elif red_rect_y > screen_height - rect_size:
        red_rect_y = screen_height - rect_size

    
    green_rect_y = red_rect_y - 60
    green_rect_x = red_rect_x
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, red_color, (red_rect_x, red_rect_y, rect_size, rect_size))
    pygame.draw.rect(screen, green_color, (green_rect_x, green_rect_y, rect_size, rect_size))
    pygame.draw.rect(screen, (0, 0, 0), (end_rect_x, end_rect_y, rect_size * 2, rect_size))

    
    if red_rect_x >= end_rect_x and green_rect_x >= end_rect_x:
        font = pygame.font.SysFont(None, 64)
        text = font.render('with trust I will follow you', True, (255, 0, 0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    
    pygame.display.update()

pygame.quit()

print("我们的爱是信任和跟随")
for i in range(3):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)



import pygame
import random

pygame.init()


screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red and Green Blocks")


block_size = 50
red_block = pygame.Surface((block_size, block_size))
red_block.fill((255, 0, 0))
green_block = pygame.Surface((block_size, block_size))
green_block.fill((0, 255, 0))


red_x, red_y = 100, screen_height//2 - block_size//2
green_x, green_y = screen_width - 100 - block_size, screen_height//2 - block_size//2
white_x, white_y = screen_width//2 - block_size//2, screen_height//2 - block_size//2


red_move_x, red_move_y = 0, 0


game_running = True


clock = pygame.time.Clock()


font = pygame.font.SysFont('Arial', 20)
text = font.render('We each grow in our own way, Yet towards each other we do stray.', True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width/2, 50))


end_block = pygame.Surface((block_size, block_size))
end_block.fill((255, 255, 255))
end_x, end_y = screen_width // 2 - block_size // 2, screen_height // 2 - block_size // 2


while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if red_x > 0:
            red_move_x = -1
    elif keys[pygame.K_RIGHT]:
        if red_x < screen_width - block_size:
            red_move_x = 1
    else:
        red_move_x = 0

    if keys[pygame.K_UP]:
        if red_y > 0:
            red_move_y = -1
    elif keys[pygame.K_DOWN]:
        if red_y < screen_height - block_size:
            red_move_y = 1
    else:
        red_move_y = 0

    
    red_x += red_move_x
    red_y += red_move_y

    green_move_x = -red_move_x
    green_move_y = -red_move_y

  
    green_x += green_move_x
    green_y += green_move_y

    screen.fill((0, 0, 0))
    screen.blit(red_block, (red_x, red_y))
    screen.blit(green_block, (green_x, green_y))
    screen.blit(end_block, (end_x, end_y))
    screen.blit(text, text_rect)
    if red_x == end_x and green_x == end_x:
      
        font = pygame.font.SysFont('Arial', 50)
        text = font.render('We will reunion', True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2+100))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        game_running = False

  
    pygame.display.flip()
pygame.quit()

print("爱是我们各自成长，又彼此奔赴")
for i in range(2):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)

print("我们的爱还有很多很多的内容！")
for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("爱是从悄悄话到手写信，我总有话想告诉温柔的你；")
for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("爱是从小兔灯到新桌游，我总有礼物想送给可爱的你；")
for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("爱是一道菜放了三根二荆条，爱是热了又热的罗宋汤。")
for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("爱是传教士体位，爱是你吻我的嘴角。")
for i in range(1):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
print("爱是我们携手走过的四年")
for i in range(2):
    print(str(int(time.time()))[-2 :1])
    time.sleep(1)
import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()


t.goto(0, -150)
t.color('#ff6b6b')
t.begin_fill()
t.left(45)
t.forward(200)
t.circle(80, 225)
t.right(180)
t.circle(80, 225)
t.forward(200)
t.end_fill()

t.color('#000000')
t.goto(-250, 250)
t.write("happy 4th anniversary", font=("Arial", 40, "normal"))

turtle.done()
