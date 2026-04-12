import streamlit as st 

st.header("Generator ,Iterator, Iterable")
st.write("### Author - Kuntal")
st.write("""Generator Function
A range function create a range of value and if we wish to print it through a for loop, the result will be printing of the sequence of 0 to N range values:""")


n = st.number_input("Enter Your Number :")
n=int(n)
if n:
  st.code(f'''
  def range({n}):
      for i in range(0, {n}):
          yield i
  ''', language='python')

# Output dikhao
  for i in range(5):
      st.write(i)

  st.write(f"""This method will consume more memory as it is returning all the numbers all together.
To avoid the memory consumtion problem we can use GENERATOR function which will help to print up to which number we want to see.
Example:

Geting a Range of Value 0-100 and printing only first 5 values""")
  
  st.code(f"""def test1_range(n):
    for i in range (0,n):
        
        yield i       # in place of return provide (yield) key word
        

  #create an object of the function
  g1=test1_range(100)
  st.write("It will not print anything but the object type see below\n")
  st.write(g1) # it will not print anything but the object type
  st.write("#"*80)
  st.write()

  st.write("Upon calling the object with next key word it will print the range of the number one by one see below\n")
  st.write(next(g1))
  st.write(next(g1))
  st.write(next(g1))
  st.write(next(g1))
  st.write(next(g1))
  st.write()""")

  def test1_range(n):
    for i in range (0,n):
        
        yield i       # in place of return provide (yield) key word
        

  #create an object of the function
  g1=test1_range(100)
  st.write("It will not print anything but the object type see below\n")
  st.write(type(g1)) # it will not print anything but the object type
  st.write("#"*80)
  st.write()

  st.write("Upon calling the object with next key word it will print the range of the number one by one see below\n")
  st.write(next(g1))
  st.write(next(g1))
  st.write(next(g1))
  st.write(next(g1))
  st.write(next(g1))
  st.write()


  st.write(f"""Creating a Fibonaci series with generator Function and printing first 10 numbers one by one then print rest numbers in one go""")

  st.code(f"""# create the function
  def test1_fib(n):
      a, b= 0, 1
      for i in range(0,n):
          yield a
          a,b=b, a+b

  g2=test1_fib(20) # create the object
  print(next(g2)) # printing one by one
  print(next(g2))
  print(next(g2))
  print(next(g2))
  print(next(g2))
  print(next(g2))
  print(next(g2))
  print(next(g2))
  print(next(g2))
  print(next(g2))

  print("*"*80)
  print()
  print("Getting remaining numbers in one go\n")
  for remaining in g2: # Getting remaining numbers in one go
      print(remaining)
      """)
    
    # create the function
  def test1_fib(n):
      a, b= 0, 1
      for i in range(0,n):
          yield a
          a,b=b, a+b

  g2=test1_fib(20) # create the object
  st.write(next(g2)) # printing one by one
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))
  st.write(next(g2))

  st.write("*"*80)
  st.write()
  st.write("Getting remaining numbers in one go\n")
  for remaining in g2: # Getting remaining numbers in one go
      st.write(remaining)
      
  st.write(f"""String in Generator function and print 6 words one by one""")

  st.code(f"""def test_3_string(string):
      for i in iter(string): # making the string as iterator 
          yield (i)
          
          
  g3= test_3_string("Python Anaconda") # creating the generator object
  print(next(g3))
  print(next(g3))
  print(next(g3))
  print(next(g3))
  print(next(g3))
  print(next(g3))""")


  def test_3_string(string):
      for i in iter(string): # making the string as iterator 
          yield (i)
          
          
  g3= test_3_string("Python Anaconda") # creating the generator object
  st.write(next(g3))
  st.write(next(g3))
  st.write(next(g3))
  st.write(next(g3))
  st.write(next(g3))
  st.write(next(g3))

  st.subheader("Iterator")
  st.write(f"""Iterator
  An iterator is an object (like a pointer) that points to an element inside the container. We can use iterators to move through the contents of the container.""")

  st.write()

  st.subheader("Iterable")
  st.write(f"""Iterable
  The objects which can be converted to an Iterator are called Iterable example : string, list, tuples, set, dict.""")
  st.write("..........................................")
  st.write(f"""Note:
  Numbers are not iterable
  Space is not iterable""")

  st.subheader(f"""How to convert an Iterable to Iterator ?""")
  st.write("""Ans:\n

  Type casting with iter inbuilt function""")

  st.code(f"""text_1= "I am learning Iterable and Iterator"
  print("Before type casting")
  print()
  print(type(text_1)) # before type casting
  print("*"*80)
  print("After type casting")
  text_1= iter(text_1)
  type(text_1) """)


  text_1= "I am learning Iterable and Iterator"
  st.write("Before type casting")
  st.write()
  st.write(type(text_1)) # before type casting
  st.write("*"*80)
  st.write("After type casting")
  text_1= iter(text_1)
  type(text_1) 

  st.code(f"""# create the function 

  def test_4_strinf(n):
      n= iter(n)
      for i in n:
          yield i # make the function a generator function
  g4= test_3_string("This world is Beautiful") # create the object

  print(next(g4)) # print first 5 letters of the string 
  print(next(g4))
  print(next(g4))
  print(next(g4))
  print(next(g4))
  print(next(g4))
  print(next(g4))
  print(next(g4)) """)


  # create the function 

  def test_4_strinf(n):
      n= iter(n)
      for i in n:
          yield i # make the function a generator function
  g4= test_3_string("This world is Beautiful") # create the object

  st.write(next(g4)) # st.write first 5 letters of the string 
  st.write(next(g4))
  st.write(next(g4))
  st.write(next(g4))
  st.write(next(g4))
  st.write(next(g4))
  st.write(next(g4))
  st.write(next(g4)) 

  st.subheader(f"""Conculsion
  [yield] function make a function to a generator function
  to print one by one number need to use [next] function
  to convert an iterable to iterator do type casting with [iter] function""")

