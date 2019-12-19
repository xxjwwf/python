name='xiejiawen'
pwd='123'
count=0
while count<3:
    name_input=input('请输入用户名：')
    pwd_input=input('请输入密码：')
    if name_input != name or pwd != pwd_input:  ##尽量不使用不等判断，而使用相等判断
        print('用户名或密码错误！')
        count+=1
        continue
    else:
        print('登陆成功！用户名：',name_input,'密码：',pwd_input)
        count=3

        