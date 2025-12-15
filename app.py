def main():
    try:
        n = int(input("\nВведіть кількість членів прогресії:\n"))
        
        if n <= 0:
            print("Помилка: n має бути більше 0")
            return
     
        a1 = 2
        d = 2
        

        sum_formula = n * (2 * a1 + (n - 1) * d) // 2
        
    
        sum_loop = 0
        progression = [] 
        
        for i in range(n):
            term = a1 + i * d
            progression.append(term)
            sum_loop += term
        
       
        
        print(f"Перші {n} членів прогресії: {progression}")
        print(f"Сума через формулу: {sum_formula}")
        print(f"Сума через цикл: {sum_loop}")
        
        if sum_formula == sum_loop:
            print(f"Сума перших {n} членів = {sum_formula}")
        else:
            print("Помилка у обчисленнях")
            
    except ValueError:
        print("Помилка: введіть ціле число!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
