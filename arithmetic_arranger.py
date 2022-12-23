def arthmetic_arranger(problems):
    if len(problems) > 5:
        return print('Error: Too many problems.')

    else:
        #Vamos a definir funciones para comprobar formatos    
        #Función para comprobar el formato del operador
        def operator_proof(operator):
            if operator not in list(['+', '-']):
                return False 

            else:
                return operator

        #Función para comprobar el formato de los números
        def numbers_proof(number):
            try:
                number = int(number)
            
            except:
                return False

            else:
                return number

        #funcion para comprobar dígitos
        def digits_proof(number):

            if number >= 10000:
                return False
                
            else:
                return number


        #########################################################
        #A partir de aquí vamos a trabajar con cada uno de los problemas

        arranged = []
        for x in range(0,len(problems)):
            parts = problems[x].split()
            operand1 = parts[0]
            operand2 = parts[2]
            operator = parts[1]

            if operator == '+':
                try:
                    result = int(operand1) + int(operand2)
                except:
                    pass
            else:
                try:
                    result = int(operand1) - int(operand2)
                except:
                    pass


            #########################################################
            #Comprobamos formato de cada una de las partes del problema
            #Comprobamos operator
            if operator_proof(operator) == False:
                return print('Error: Operator must be + or -.')
            else:
                operator = operator_proof(operator)

            #Comprobamos operand1
                #formato
            if numbers_proof(operand1) == False:
                return print('Error: Numbers must only contain digits.')
            else:
                operand1 = numbers_proof(operand1)

                #dígitos
            if digits_proof(operand1) == False:
                return print('Error: Numbers cannot be more than four digits.')
            else:
                operand1 = digits_proof(operand1)

            #Comprobamos operand2
                #formato
            if numbers_proof(operand2) == False:
                return print('Error: Numbers must only contain digits.')
            else:
                operand2 = numbers_proof(operand2)

                #dígitos
            if digits_proof(operand2) == False:
                return print('Error: Numbers cannot be more than four digits.')
            else:
                operand2 = digits_proof(operand2)

            ###########################################################
            #Una vez comprobado el formato, vamos a posicionar la salida
            #Condiciones de formato para la salida
            if max(int(operand1), int(operand2)) < 10:
                line = '---'
                space1 = 3
                space2 = 1
            else:
                if max(int(operand1), int(operand2)) < 100:
                    line = '----'
                    space1 = 4
                    space2 = 2
                else:
                    if max(int(operand1), int(operand2)) < 1000:
                        line = '-----'
                        space1 = 5
                        space2 = 3
                    else:
                        line = '------'
                        space1 = 6
                        space2 = 4

                #Salida
            
            arranged.append([str(operand1).rjust(space1), operator, str(operand2).rjust(space2), line, str(result).rjust(space1)])
        
        
        ##Ahora que tenemos la salida, definimos las líneas para el print
        if len(problems) == 1:
            line1 = [arranged[0][0]]
            line2 = [[arranged[0][1], arranged[0][2]]]
            line3 = [arranged[0][3]]
            line4 = [arranged[0][4]]
        else:
            if len(problems) == 2:
                line1 = [[arranged[0][0], arranged[1][0]]]
                line2 = [[arranged[0][1], arranged[0][2], arranged[1][1], arranged[1][2]]]
                line3 = [[arranged[0][3], arranged[1][3]]]
                line4 = [[arranged[0][4], arranged[1][4]]]
            else:
                if len(problems) == 3:
                    line1 = [[arranged[0][0], arranged[1][0], arranged[2][0]]]
                    line2 = [[arranged[0][1], arranged[0][2], arranged[1][1], arranged[1][2], arranged[2][1], arranged[2][2]]]
                    line3 = [[arranged[0][3], arranged[1][3], arranged[2][3]]]
                    line4 = [[arranged[0][4], arranged[1][4], arranged[2][4]]]
                else:
                    if len(problems) == 4:
                        line1 = [[arranged[0][0], arranged[1][0], arranged[2][0], arranged[3][0]]]
                        line2 = [[arranged[0][1], arranged[0][2], arranged[1][1], arranged[1][2], arranged[2][1], arranged[2][2], arranged[3][1], arranged[3][2]]]
                        line3 = [[arranged[0][3], arranged[1][3], arranged[2][3], arranged[3][3]]]
                        line4 = [[arranged[0][4], arranged[1][4], arranged[2][4], arranged[3][4]]]
                    else:
                        line1 = [[arranged[0][0], arranged[1][0], arranged[2][0], arranged[3][0], arranged[4][0]]]
                        line2 = [[arranged[0][1], arranged[0][2], arranged[1][1], arranged[1][2], arranged[2][1], arranged[2][2], arranged[3][1], arranged[3][2], arranged[4][1], arranged[4][2]]]
                        line3 = [[arranged[0][3], arranged[1][3], arranged[2][3], arranged[3][3], arranged[4][3]]]
                        line4 = [[arranged[0][4], arranged[1][4], arranged[2][4], arranged[3][4], arranged[4][4]]]
        

        ##Finalmente con las líneas de salida, definimos arranged_problems como el print
        if len(problems) == 1:
            arranged_problems = print(line1[0][0],'\n',
                            line2[0][0],' ', line2[0][1],'\n',
                            line3[0][0],'\n',
                            line4[0][0], sep='')
        else:
            if len(problems) == 2:
                arranged_problems = print(line1[0][0], '    ', line1[0][1],'\n',
                            line2[0][0],' ', line2[0][1], '    ', line2[0][2], ' ', line2[0][3],'\n',
                            line3[0][0], '    ', line3[0][1],'\n',
                            line4[0][0], '    ', line4[0][1], sep='')
            else:
                if len(problems) == 3:
                    arranged_problems = print(line1[0][0], '    ', line1[0][1], '    ', line1[0][2],'\n',
                            line2[0][0],' ', line2[0][1], '    ', line2[0][2], ' ', line2[0][3], '    ', line2[0][4], ' ', line2[0][5],'\n',
                            line3[0][0], '    ', line3[0][1], '    ', line3[0][2],'\n',
                            line4[0][0], '    ', line4[0][1], '    ', line4[0][2], sep='')
                else:
                    if len(problems) == 4:
                        arranged_problems = print(line1[0][0], '    ', line1[0][1], '    ', line1[0][2], '    ', line1[0][3],'\n',
                            line2[0][0],' ', line2[0][1], '    ', line2[0][2], ' ', line2[0][3], '    ', line2[0][4], ' ', line2[0][5], '    ', line2[0][6], ' ', line2[0][7],'\n',
                            line3[0][0], '    ', line3[0][1], '    ', line3[0][2], '    ', line3[0][3],'\n',
                            line4[0][0], '    ', line4[0][1], '    ', line4[0][2], '    ', line4[0][3], sep='')
                    else:
                        arranged_problems = print(line1[0][0], '    ', line1[0][1], '    ', line1[0][2], '    ', line1[0][3], '    ', line1[0][4],'\n',
                            line2[0][0],' ', line2[0][1], '    ', line2[0][2], ' ', line2[0][3], '    ', line2[0][4], ' ', line2[0][5], '    ', line2[0][6], ' ', line2[0][7], '    ', line2[0][8], ' ', line2[0][9],'\n',
                            line3[0][0], '    ', line3[0][1], '    ', line3[0][2], '    ', line3[0][3], '    ', line3[0][4],'\n',
                            line4[0][0], '    ', line4[0][1], '    ', line4[0][2], '    ', line4[0][3], '    ', line4[0][4], sep='')

    
    ##La salida sería
    return arranged_problems

    

arthmetic_arranger(['3801 + 2456'])