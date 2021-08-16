'''
This program explains how classes work in python. by designing a simple class
with multiple methods and attributes, to allow easy adjustment on the code in the future.
the program contains default data.
the program also shows the concepts of accesors and mutators functions, inside the class.

Name: JOHN MILHAIL

'''
# class declaration
class ShippingCharges:

    # constructor with default values
    def __init__(self, companyName="FedEx", userName="John Smith", packageCount=0, shipmentWeight=0, totalCost=0):
        # set fields equal to passed variables
        self.companyName = companyName
        self.userName = userName
        self.packageCount = packageCount
        self.shipmentWeight = shipmentWeight
        self.totalCost = totalCost

    # accessor
    def getCompanyName(self):
        return self.companyName

    # mutator
    def setCompanyName(self, companyName):
        self.companyName = companyName

    # accessor
    def getUserName(self):
        return self.userName

    # mutator
    def setUserName(self, userName):
        self.userName = userName

    # accessor
    def getPackageCount(self):
        return self.packageCount

    # mutator
    def setPackageCount(self, packageCount):
        self.packageCount = packageCount

    # accessor
    def getShipmentWeight(self):
        return self.shipmentWeight

    # mutator
    def setShipmentWeight(self, shipmentWeight):
        self.shipmentWeight = shipmentWeight

    # print function
    def printInformation(self):
        print("Name: " + str(self.userName))
        print("Number of packages: " + str(self.packageCount))
        print("Total charges: $ %.2f " %(self.totalCost))

# greeting the user function
def Greeting():
    name = input("please enter your full name: <first and last name> : ")
    print("\n")
    print("Hello", name)
    print("\n")
    print("this program will ask you to enter the weights of your packages.")
    print("To calculate the total amount of charges required to ship those packages.\n ")
    return name


# calculating the charge function
def PackageCharge(weight):
    if (weight <= 2):
        c = weight * 1.1
    elif (2 < weight <= 6):
        c = weight * 2.2
    elif (6 < weight <= 10):
        c = weight * 3.7
    elif (weight > 10):
        c = weight * 3.8
    return (c)


# the program driver function
def main():
    name = Greeting()

    i = 'y'
    data = []
    shipmentWeight = 0
    packageCount = 0
    charge = 0
    while (i == 'y'):
        packageCount += 1
        print("\n")
        Lb = eval(input("please enter the weight of your package: "))
        if(Lb>0):
            shipmentWeight += Lb
            c = PackageCharge(Lb)
            print("the shipping fee for this package is $ %.2f" %(c))
            print('\n')
            i = input("Do you want to add another package? <y/n>: ")
            data.append(c)
            charge = sum(data)

        elif(Lb<0):

            while(Lb<0):
                Lb1 = eval(input('please re-enetr a positive value for the weight: '))
                if(Lb1>0):
                    break
            shipmentWeight += Lb1
            c = PackageCharge(Lb1)
            print("the shipping fee for this package is $ %.2f" %(c))
            print('\n')
            i = input("Do you want to add another package? <y/n>: ")
            data.append(c)
            charge = sum(data)
            
    print('\n')
    shippingCharges = ShippingCharges()
    shippingCharges.printInformation()
    print('\n')

    shippingCharges = ShippingCharges("Amazon Prime", "Test Name", 2, 10, 22)
    shippingCharges.printInformation()
    print('\n')

    shippingCharges = ShippingCharges("UPS", name, packageCount, shipmentWeight, charge)
    shippingCharges.printInformation()


# intiate main()
main()
