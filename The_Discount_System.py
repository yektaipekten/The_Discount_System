# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:52:01 2023

@author: yekta
"""

class Customer:                      # I am really sorry I couldn't find the correct code
    
    
    def __init__(self, name, memberType):
        self.name = name
        self.memberType = memberType
        
        def Customer(self,name):
            pass
        
        def isMember(self):
            pass
        
        def getName(name):
            pass
        
        def setName(name):
            pass
        
        def getMemberType():
            pass
        
        def setMemberType():
            pass
        
        def toString():
            pass
        
        
class DiscountRate:
    def __init__(self, ServicePremium, ServiceGold, ServiceSilver, 
                 ProductPremium, ProductGold, ProductSilver):
        self.ServicePremium = ServicePremium
        self.ServiceGold = ServiceGold
        self.ServiceSilver = ServiceSilver
        self.ProductPremium = ProductPremium
        self.ProductGold = ProductGold
        self.ProductSilver = ProductSilver
        
        
class Visit:
    def __init__(self,customer, discountrate, serviceExpense, productExpense): # (self,c,d, se=0,pe=0)
        self.customer = customer
        self.discountrate = discountrate
        self.serviceExpense = serviceExpense
        self.productExpense = productExpense
        
    def get_Total_Expense(self):
        discountrate = DiscountRate()
        
    def Calculate_Total_Expense(self):
        if self.customer.memberType == 'Premium':
            ServiceDiscount = self.serviceExpense * self.discountrate.ServicePremium
            ProductDiscount = self.productExpense * self.discountrate.ProductPremium 
        elif self.customer.memberType == 'Gold':
            ServiceDiscount = self.serviceExpense * self.discountrate.ServiceGold
            ProductDiscount = self.productExpense * self.discountrate.ProductGold
        elif self.customer.memberType == 'Silver':
            ServiceDiscount = self.serviceExpense * self.discountrate.ServiceSilver
            ProductDiscount = self.productExpense * self.discountrate.ProductSilver
        else:
            ServiceDiscount = 0
            ProductDiscount = 0
            
        TotalCharge = self.serviceExpense - ServiceDiscount + self.productExpense - ProductDiscount
        return TotalCharge
    def get_Total_expense(memberType, serviceExpense, productExpense):
        discountrate = DiscountRate(0.2, 0.15 ,0.10, 0.10 ,0.10 ,0.10)
        customer = Customer("", memberType)
        visit = Visit(customer, serviceExpense, productExpense, discountrate)
        TotalCharge = visit.Calculate_Total_Expense()
        return TotalCharge


    def __repr__(self):
        pass
  
    def Visit(self, name, date):
        pass
    
    def getName():
        pass
    
    def getServiceExpense():
        pass
    
    def setServiceExpense(ex):
        pass
    
    def getProductExpense():
        pass
    
    def setProductExpense(ex):
        pass
    
    def toString():
        pass
    

discountrate = DiscountRate(0.2, 0.15 ,0.10, 0.10 ,0.10 ,0.10)

customer = Customer("yek ipek","Premium")

visit = Visit(customer, 100, 50, discountrate) 

TotalCharge = visit.Calculate_Total_Expense()

print(f"Total Expense:{TotalCharge}")
