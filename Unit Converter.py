print("        UNIT CONVERTER        ")
print("Quantities Available:")
print("1.Length")
print("2.Weight/Mass")
print("3.Time")
print("4.Temperature")
print("5.Area")
print("6.Volume")
print("7.Speed")
print("8.Data Storage")
print("")
quant=input("Enter the quantity: ").lower()
if quant in ['1','1.','length']:
    print("")
    print("Units Available: ")
    print("1.Millimeter(mm)")
    print("2.Centimeter(cm)")
    print("3.Meter(m)")
    print("4.Kilometer(km)")
    print("5.Inch")
    print("6.Foot")
    print("7.Yard")
    print("8.Mile")
    print("")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("mm", 1),
    "2": ("cm", 10),
    "3": ("m", 1000),
    "4": ("km", 1000000),
    "5": ("in", 25.4),
    "6": ("ft", 304.8),
    "7": ("yd", 914.4),
    "8": ("mile", 1609344)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
elif quant in ['2','2.','mass','weight','weight/mass','mass/weight']:
    print("")
    print("Units Available: ")
    print("1.Milligram(mg)")
    print("2.Gram(g)")
    print("3.Kilogram(kg)")
    print("4.Tonne")
    print("5.Ounce")
    print("6.Pound")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("mg", 1),
    "2": ("g", 1000),
    "3": ("kg", 1000000),
    "4": ("tonne", 1e+9),
    "5": ("ounce", 28349.5),
    "6": ("lbs", 453592.000004704)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
elif quant in ['3','3.','time']:
    print("")
    print("Units Available: ")
    print("1.Second(s)")
    print("2.Minute(min)")
    print("3.Hour(hr)")
    print("4.Day(d)")
    print("5.Week(wk)")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("s", 1),
    "2": ("min", 60),
    "3": ("hr", 3600),
    "4": ("day", 86400),
    "5": ("week", 604800)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
elif quant in ['4','4.','temp','temperature']:
    print("")
    print("Units Available: ")
    print("1.Celsius(C)")
    print("2.Fahrenheit(F)")
    print("3.Kelvin(K)")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    if iunit in ['1','1.'] and ounit in ['2','2.']:
        tempans=(inpt * 9/5) + 32
        print("Answer is", tempans, ' Fahrenheit')
    elif iunit in ['1','1.'] and ounit in ['3','3.']:
        tempans=inpt+273.15
        print("Answer is", tempans, ' Kelvin')
    elif iunit in ['2','2.'] and ounit in ['1','1.']:
        tempans=(inpt - 32) * 5/9
        print("Answer is", tempans, ' Celsius')
    elif iunit in ['2','2.'] and ounit in ['3','3.']:
        tempans=(inpt - 32) * 5/9 + 273.15
        print("Answer is", tempans, ' Kelvin')
    elif iunit in ['3','3.'] and ounit in ['1','1.']:
        tempans=inpt - 273.15
        print("Answer is", tempans, ' Celsius')
    elif iunit in ['3','3.'] and ounit in ['2','2.']:
        tempans=(inpt - 273.15) * 9/5 + 32
        print("Answer is", tempans, ' Fahrenheit')
    elif iunit == ounit:
        print("both units cant be same")
    else:
        print("invalid choice")
elif quant in ['5','5.','area']:
    print("")
    print("Units Available: ")
    print("1.Square Centimetre(cm2)")
    print("2.Square Metre(m2)")
    print("3.Square Kilometre(km2)")
    print("4.Square Foot")
    print("5.Acre")
    print("6.Hectare")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("Square centimetre (cm²)", 1),
    "2": ("Square metre (m²)", 10000),
    "3": ("Square kilometre (km²)", 1e10),
    "4": ("Square foot (ft²)", 929.0304),
    "5": ("Acre", 40468564.224),
    "6": ("Hectare (ha)", 1e8)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
elif quant in ['6','6.','volume','vol']:
    print("")
    print("Units Available: ")
    print("1.Millilitre(mL)")
    print("2.Litre(L)")
    print("3.Cubic metre(m3)")
    print("4.Galon(US)")
    print("5.Cup(US)")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("Millilitre (mL)", 1),
    "2": ("Litre (L)", 1000),
    "3": ("Cubic metre (m³)", 1e6),
    "4": ("Gallon (US)", 3785.411784),
    "5": ("Cup (US)", 236.5882365)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
elif quant in ['7','7.','speed']:
    print("")
    print("Units Available: ")
    print("1.Metres per second (m/s)")
    print("2.Kilometres per hour (km/h)")
    print("3.Miles per hour (mph)")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("Metres per second (m/s)", 1),
    "2": ("Kilometres per hour (km/h)", 0.2777777778),
    "3": ("Miles per hour (mph)", 0.44704)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
elif quant in ['8','8.','data','data storage']:
    print("")
    print("Units Available: ")
    print("1.Bit")
    print("2.Byte")
    print("3.Kilobyte (KB)")
    print("4.Megabyte (MB)")
    print("5.Gigabyte (GB)")
    print("6.Terabyte (TB)")
    iunit=input("Select Input Unit: ")
    ounit=input("Select Output Unit: ")
    inpt=float(input("Enter the input value: "))
    units = {
    "1": ("Bit", 1),
    "2": ("Byte", 8),
    "3": ("Kilobyte (KB)", 8192),
    "4": ("Megabyte (MB)", 8388608),
    "5": ("Gigabyte (GB)", 8589934592),
    "6": ("Terabyte (TB)", 8796093022208)}
    input_unit = units[iunit]
    output_unit = units[ounit]
    ans = inpt * input_unit[1] / output_unit[1]
    print("Answer is", ans, output_unit[0])
else:
    print("Invalid choice")