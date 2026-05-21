# Databricks notebook source
empno=int(input("enter the empno :"))
ename=input("enter the ename :")
esal=float(input("enter the esal :"))

ta=esal*10/100
da=esal*15/100
hra=esal*20/100
total_allow=(ta+da+hra)
gross_sal=esal+total_allow

print("\t\t employee payslip")
print("-" * 50)
print("\t employee_number :", empno)
print("\t employee_name :", ename)
print("\t employee_salary :", esal)
print("\n\t employee ta :", ta)
print("\t employee da :", da)
print("\t employee hra :",hra)
print("\t employee total_allowances :",total_allow)
print("\t employee gross_salary :",gross_sal)
print("-" * 50)


# COMMAND ----------

print("hello world")
print("i'm raviteja padimi")
print("i'm senior data engineer")

