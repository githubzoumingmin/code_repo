message="hello world";
print(message);
name="zou ming ming";
print(name.title());
print(name.upper());
name=name.title();
print(name.lower());
first_name="zou";
last_name="ming ming";
full_name=f"{first_name} {last_name}";
print(full_name.title() + " is a good boy");
file_name="hello_world.py";
print(file_name.removesuffix(".py"));
x,y,z=1,2,3;
print(x,y,z);
print(x)
MAX_CONNECTIONS=100;
# 常量通常使用全大写字母和下划线命名，以便与变量区分开来
print(MAX_CONNECTIONS);
arr=[64, 34, 25, 12, 22, 11, 90];
print(arr[1])
print(arr[-1]);
arr.append(100);
print(arr);
del arr[2];
print(arr);
arr.insert(2, 25);
print(arr);
pop_value=arr.pop();
print(pop_value);
print(arr);
arr.pop(2);
print(arr);
arr.insert(2, 22);
print(arr);
arr.remove(22);
print(arr);
info={"name":"Alice","age":30,"city":"New York"};
for key,value in info.items():
    print(f"{key}: {value}");

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort();
for car in cars:
    print(f"{car.title()} is a nice car.");
print(car);
for num in range(0,6,2):
    print(num);
numbers=list(range(1,11));
print(numbers);
squares=[];
# for num in range(1,11):
#     squares.append(num**2);
# print(squares);
squares=[num**2 for num in range(1,11)];
print(squares);
print(min(squares));
print(max(squares));
print(sum(squares));
for value in range(1,20,2):
    print(value);
for value in range(3,30,3):
    print(value);
numbers=[value**3 for value in range(1,11)];
print(numbers);
players=['charles','martina','michael','florence','eli'];
print(players[0:3]);
print(players[1:4]);
print(players[:4]);
print(players[1:]);
print(players[1:4:2]);
my_foods=['pizza','falafel','carrot cake'];
friend_foods=my_foods[:];
print("My favorite foods are:");
print(my_foods);    
print("\nMy friend's favorite foods are:");
print(friend_foods);
cars=['bmw','audi','toyota','subaru'];
print("Here is the original list:");
for car in cars:
    if car=='bmw':
        print(car.upper());
    else:        
        print(car.title());
flg="bmw" in cars;
print("bwm" not in cars);
age=19;
if age>=18:
    print("You are old enough to vote!");
age=17;
if age>=18:
    print("You are old enough to vote!"); 
else:
    print("Sorry, you are too young to vote.");
age=14
if age<4:
    prince=0;
elif age<18:
    prince=5;
else:  
    prince=10;
print(f"Your admission cost is ${prince}.");
requested_toppings=[];
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!");
else:
    print("Are you sure you want a plain pizza?");
demands=(10,20);
print(demands);
demands=(20,30);
print(demands);
str="";
if str:
    print("The string is not empty.");
else:
    print("The string is empty.");
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese'];
requested_toppings=['mushrooms','french fries','extra cheese'];
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!");
names=["zmm","alice","bob","carl","admin"];
for name in names:
    if name=="admin":
        print(f"Hello {name.title()},would you like to see a status report?");
    else:
        print(f"Hello {name.title()},thank you for logging in again.");
current_users=['alice','bob','carl','dave','eve'];
new_users=['Alice','Bob','Frank','Grace','Heidi'];
current_users_lower=[user.lower() for user in current_users];
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.");
    else:
        print(f"The username '{new_user}' is available.");
numbers=list(range(1,10));
for number in numbers:
    if number==1:
        print(f"{number}st");
    elif number==2:
        print(f"{number}nd");
    elif number==3:
        print(f"{number}rd");
    else:
        print(f"{number}th");
alien_color={'color':'green','points':5};
print(alien_color);
alien_color["x"]=0;
alien_color["y"]=25;
print(alien_color);
alien_0={'color':'green','points':5,'x':0,'y':25,"speed":'slow'};
if alien_0["speed"]=="slow":
    x_increment=1;
elif alien_0["speed"]=="medium":
    x_increment=2;
else:
    x_increment=3;
alien_0["x"]+=x_increment;
print(alien_0);
del alien_0["points"];
print(alien_0);
point_value=alien_0.get("points","No points value assigned.");
print(point_value);
point_value=alien_0.get("points");
print(point_value);
pepole={'name':'Alice','age':30,'city':'New York'};
for key,value in pepole.items():
    print(f"{key}: {value}");
for key in pepole.keys():
    print(key);
for value in pepole.values():
    print(value);
for key in pepole:
    print(key);
nums=[7,1,2,3,4,5];
nums.sort();
print(nums);
favorite_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'};
list_values=list(favorite_languages.values());
set_values=set(favorite_languages.values());
print(list_values);
print(set_values);
nums=range(11);
list_nums=list(nums);
print(list_nums);
for num in nums:
    list_nums.append(num);
print(list_nums);
# input()函数用于从用户那里获取输入，输入的数据类型默认为字符串
# name=input("Please enter your name: ");
# print(f"\nHello, {name}!");
# prompt="If you tell us who you are, we can personalize the messages you see.";
# prompt+="\nWhat is your first name? ";
# first_name=input(prompt);
# print(f"\nHello, {first_name}!");
age=input("How old are you? ");
age=int(age);
if age>=18:
    print("You are old enough to vote!");