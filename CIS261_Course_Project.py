def getEmpName():
    empName = input("Enter employee name:  ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours worked:  "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate:  "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate:  "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxandNetPay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printinfo(empName, hours, hourlyRate, grossPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
    
def printtotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal number of employees: {totalEmployees}")
    print(f"Total hours worked: {totalHours:,.2f}")
    print(f"Total gross pay: {totalGrossPay:,.2f}")
    print(f"Total taxes: {totalTax:,.2f}")
    print(f"Total net pay: {totalNetPay:,.2f}")

if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        grossPay, incomeTax, netPay = CalcTaxandNetPay(hours, hourlyRate, taxRate)
        
        print(empName, hours, hourlyRate, grossPay, taxRate, incomeTax, netPay)
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grossPay
        totalTax += incomeTax
        totalNetPay += netPay
     
printtotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)
    
    
