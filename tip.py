def tc(b_a,tip_perc):
    total=b_a*(1+0.01*tip_perc)
    total=round(total,2)  
    print("Please pay ${total}")
tc(150,20)