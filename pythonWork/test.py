#!usr/bin/python
# -*- coding:UTF-8 -*-

# import copy
#
#
# triangle = []
#
# for n in range(2):
#     temp = copy.copy(triangle)
#     for i in range(1, len(temp)):
#         triangle[i] = temp[i] + temp[i-1]
#     triangle.append(1)
#
#     print(str(triangle).replace('[', '  ').replace(']', '  ').center(100, '*'))

# for x in range(1, 20):
#     for y in range(1, 33):
#         for z in range(1, 100):
#             if 5 * x + 3 * y + z == 100:
#                 if x + y + 3 * z == 100:
#                     print('*'*50)
#                     print('gongji is %s' % x)
#                     print('muji is %s' % y)
#                     print('xiaoji is %s' % (3 * z))

# import random
#
# print('*'*50)
# temp = []
# print('随机验证码 :', end='')
# for _ in range(4):
#     ran = chr(random.randint(50, 100))
#     print(ran, end='')
#     temp.append(ran)
# print()
# rec = input('输入的验证码 : ')
#
# if temp == list(rec):
#     print('输入正确')
# else:
#     print('输入xxx')
# import time
#
# print('*'*50)
# high_started = 100
# weight = 0.5
# high_sum = 0
# high_next = high_started
# for i in range(1,11):
#     print('Times : %s' % i)
#     high_last, high_next = high_next, high_next * weight
#     print('High is : %s' % high_next)
#     high_sum = high_sum + high_last + high_next
#     print('Length is : %s' % high_sum)
#     time.sleep(2)
#     print('-' * 50)

# last_num = lambda x: 2 * (x + 1)
# next_num = 1
# for _ in range(9):
#     next_num = last_num(next_num)
#     print(next_num)
#     print('-' * 50)

# rec = input('Please type a 5-digit number : ')
# print(rec)
# if (int(rec) > 9999) and (int(rec) < 100000):
#     number = list(rec)
#     number = number[::-1]
#     print(number)
#     print(''.join(number))
# else:
#     print('Failure input')

#
# def multiplication(fist_num, second_num):
#     if fist_num == 1:
#         return 'Done'
#     elif second_num == 1:
#         fist_num -= 1
#         second_num = fist_num
#         print('%s x 1 = %s' % (fist_num, fist_num))
#         print('-' * 50)
#         return multiplication(fist_num, second_num)
#     else:
#         print('%s x %s = %s' % (fist_num, second_num, fist_num * second_num), end=' ')
#         second_num -= 1
#         return multiplication(fist_num, second_num)
#
# multiplication(9,9)

# import os
#
# current_path = os.getcwd()
# file_path = os.path.join(current_path, 'test.py')
# new_file = os.path.splitext(file_path)[0] + 'Copy' + os.path.splitext(file_path)[1]
#
# print(file_path)
# print(new_file)
#
# with open(file_path, 'r') as fp:
#     lines = fp.readlines()
#     with open(new_file, 'w') as fp_new:
#         for line in lines:
#             fp_new.write(line)
#     fp_new.close()
#
# fp.close()

# import os
# import time
#
# current_path = os.getcwd()
# file_path = os.path.join(current_path, 'test.py')
# new_file = os.path.splitext(file_path)[0] + 'Copy' + os.path.splitext(file_path)[1]
#
# print(file_path)
# print(new_file)
#
# with open(file_path, 'r') as fp:
#     lines = fp.readlines()
#     for line in lines:
#         time.sleep(1)
#         if line.startswith('#'):
#             pass
#         else:
#             print(line, end='')
# fp.close()
# import re
#
# str1 = '     xx xxx xxadasdasd     '
# res = re.match(r'(^\s*)(.*\S)(\s*$)', str1).group(2)
#
# print(res)

# #########################Password Book ################
# import sys
# import os
# import time
# import yaml
#
#
# class HomePage(object):
#     def __init__(self):
#         self.objSignIn = None
#         self.objSignUp = None
#
#     def selection(self, signIn, signUp, account):
#         print(' Home Page '.center(50, '*'))
#         print('-> 1.Sign In')
#         print('-> 2.Sign Up')
#         print('-> 3.Exit')
#         rec = input('-> ')
#         if rec.isdigit():
#             flag = int(rec)
#             if flag == 1:
#                 time.sleep(2)
#                 self.objSignIn = signIn()
#                 self.objSignIn.selection(account)
#             elif flag == 2:
#                 time.sleep(2)
#                 self.objSignUp = signUp()
#                 self.objSignUp.selection(account)
#             elif flag == 3:
#                 print(' Exit '.center(50, '*'))
#                 sys.exit()
#             else:
#                 print('-> Type Error, Please Entry A Digital Number In 1 - 3')
#         else:
#             print('-> Type Error, Please Entry A Digital Number In 1 - 3')
#         time.sleep(2)
#         self.selection(signIn, signUp, account)
#
#     def __str__(self):
#         return '->> This Is Home Page <<-'.center(50, '*')
#
#
# class SignIn(object):
#     def __init__(self):
#         self.objHomePage = None
#         self.objAccount = None
#         self.pwd = None
#         self.acc = None
#
#     def selection(self, account):
#         print(' Sign In '.center(50, '*'))
#         print('-> 1.Back')
#         print('-> 2.Exit')
#         print('-> Or Entry Your Account to Logging ')
#         self.acc = input('-> ')
#
#         if self.acc.isdigit():
#             self.acc = int(self.acc)
#             if self.acc == 1:
#                 time.sleep(2)
#                 print(' Back '.center(50, '<'))
#                 return -1
#             elif self.acc == 2:
#                 time.sleep(2)
#                 print(' Exit '.center(50, '*'))
#                 sys.exit()
#             else:
#                 print('-> Please Entry A Digital Number In 1 - 2 ')
#         else:
#             objAccount = account()
#             ret = objAccount.checkAccount(self.acc)
#             if ret == 1:
#                 print('-> Please Entry Your Password ')
#                 self.pwd = input('-> ')
#                 ret = objAccount.checkPassword(self.acc, self.pwd)
#                 if ret == 1:
#                     return objAccount.selection()
#                 else:
#                     print('-> Password Failure ! ')
#             else:
#                 print('-> Account Failure ! ')
#
#         time.sleep(2)
#         self.selection(account)
#
#
# class Account(object):
#     def __init__(self):
#         self.acc = None
#         self.pwd = None
#         currentPath = os.getcwd()
#         self.__path = os.path.join(currentPath, 'account.yaml')
#         with open(self.__path, 'r') as fp:
#             self.accounts = yaml.load(fp)
#             fp.close()
#
#     def checkAccount(self, acc):
#         self.acc = acc
#         if self.acc in self.accounts.keys():
#             return 1
#         return -1
#
#     def checkPassword(self, acc, pwd):
#         self.acc = acc
#         self.pwd = pwd
#         if self.acc in self.accounts.keys():
#             if self.pwd == self.accounts[self.acc]:
#                 return 1
#         return -1
#
#     def selection(self):
#         print(' Welcome %s '.center(50, '*') % self.acc)
#         print('-> 1.Search')
#         print('-> 2.Modify PassWord')
#         print('-> 3.Delete Account')
#         print('-> 4.Home Page')
#         print('-> 5.Exit')
#         rec = input('-> ')
#
#         if rec.isdigit():
#             rec = int(rec)
#             if rec == 1:
#                 self.search()
#             elif rec == 2:
#                 self.modify()
#             elif rec == 3:
#                 self.delAccount()
#                 return -1
#             elif rec == 4:
#                 print(' Back '.center(50, '<'))
#                 return -1
#             elif rec == 5:
#                 print(' Exit '.center(50, '*'))
#                 sys.exit()
#             else:
#                 print('-> Please Entry A Digital Number In 1 - 6')
#         else:
#             print('-> Please Entry A Digital Number In 1 - 6')
#
#         time.sleep(1)
#         self.selection()
#
#     def search(self):
#         print(' Search '.center(50, '*'))
#         rec = input('-> Searching : ')
#         time.sleep(2)
#         if rec in self.accounts.keys():
#             print('-> The \'%s\' In Account Book !' % rec)
#         else:
#             print('-> The \'%s\' Doesn\'t In Account Book !' % rec)
#
#     def modify(self):
#         print(' Modify PassWord '.center(50, '*'))
#         print('-> Please Entry The Old Password')
#         rec = input('-> ')
#         if rec == self.pwd:
#             print('-> Please Entry The New Password')
#             new1 = input('-> ')
#             print('-> Please Confirm The New Password')
#             new2 = input('-> ')
#             if new1 == new2:
#                 self.accounts[self.acc] = new1
#
#                 with open(self.__path, 'w') as fp:
#                     yaml.dump(self.accounts, fp)
#                     fp.close()
#                 time.sleep(2)
#                 print(' Modifying Successful ! '.center(50, '*'))
#             else:
#                 time.sleep(1)
#                 print(' Twice Input Doesn\'t Matching ! '.center(50, '*'))
#         else:
#             time.sleep(1)
#             print(' Password Doesn\'t Matching ! '.center(50, '*'))
#
#     def delAccount(self):
#         print(' Delete Account '.center(50, '*'))
#         print('-> Please Entry Your Password')
#         rec = input('-> ')
#         if rec == self.pwd:
#             self.accounts.pop(self.acc)
#
#             with open(self.__path, 'w') as fp:
#                 yaml.dump(self.accounts, fp)
#                 fp.close()
#             time.sleep(2)
#             print(' Account \'%s\' Has Deleted '.center(50, '*') % self.acc)
#         else:
#             print(' Password Doesn\'t Matching ! '.center(50, '*'))
#
#     def creator(self):
#         print(' Creating Account '.center(50, '*'))
#         print('-> Please Entry Your Account')
#         rec = input('-> ')
#         if self.acc in self.accounts.keys():
#             print(' Account \'%s\' Existed'.center(50, '*') % rec)
#         else:
#             self.acc = rec
#             print('-> Please Entry Your Password')
#             self.pwd = input('-> ')
#             self.accounts[self.acc] = self.pwd
#             with open(self.__path, 'w') as fp:
#                 yaml.dump(self.accounts, fp)
#                 fp.close()
#             time.sleep(2)
#
#
# class SignUp(object):
#     def __init__(self):
#         self.objAccount = None
#         self.rec = ''
#
#     def selection(self, account):
#         print(' Sign Up '.center(50, '*'))
#         print('-> 1.Back')
#         print('-> 2.Create Account')
#         print('-> 3.Exit')
#         self.rec = input('-> ')
#         if self.rec.isdigit():
#             flag = int(self.rec)
#             if flag == 1:
#                 print(' Back '.center(50, '<'))
#                 time.sleep(2)
#                 return -1
#             if flag == 2:
#                 self.objAccount = account()
#                 self.objAccount.creator()
#                 self.objAccount.selection()
#
#             elif flag == 3:
#                 print(' Exit '.center(50, '*'))
#                 sys.exit()
#         print('-> Please Entry A Digital Number In 1 - 2 ')
#         time.sleep(2)
#         self.selection(account)
#
#
# if __name__ == "__main__":
#     test = HomePage()
#     test.selection(SignIn, SignUp, Account)
