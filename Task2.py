from dhCheck_Task2 import dhCheckCorrectness

def Task2(num, table, probs):

    row_y6 = table[0]  
    row_y7 = table[1] 
    row_y8 = table[2] 


    x3_count = row_y6[1] + row_y7[1] + row_y8[1]  
    x4_count = row_y6[2] + row_y7[2] + row_y8[2]  
    prob1 = (x3_count + x4_count) / num


    count_xy_leq_10 = (
        row_y6[0] +  
        row_y7[0] +  
        row_y8[0] +  
        row_y6[1] + 
        row_y7[1] + 
        row_y6[2]    
    )
    prob2 = count_xy_leq_10 / num

    PX2, PX3, PX4, PX5, _, _ = probs 
    
    P_Y8 = sum(row_y8) / num
    

    P_T_Y8 = (
        (PX2 * row_y8[0] / num) +  
        (PX3 * row_y8[1] / num) +  
        (PX4 * row_y8[2] / num) +  
        (PX5 * row_y8[3] / num)   
    )
    
 
    prob3 = P_T_Y8 / P_Y8 if P_Y8 > 0 else 0

    return (prob1, prob2, prob3)
