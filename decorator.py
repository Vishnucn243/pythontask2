import time    
def outfun(func):
    def infun(*args, **kwargs):
        begin= time.time()
        result = func(*args, **kwargs)
        end= time.time()
        exectime = begin-end
        print(f"execution time is  {exectime:.4f} seconds")
        return result
    
    return infun

@outfun
def fun():
   time.sleep(2)
   print("success")

fun()