# Multithreading 
# Multitasking :is running different apps at a time
# Multithreading :Running many tasks of any application

# print("start of thread")
# import threading
# import time
# class MyThread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name

#     def run(self):
#         print(f"thread is running: {self.name}")
#         # print(threading.current_thread().name)
#         # print("ABC")
#         for i in range(5):
#             print(threading.current_thread().name)
#             print("Pratiksha")
#             time.sleep(3)

# t1 = MyThread("Thread _ 1")
# t1.start()
# print("ZYX")

# print("end of thread")



import threading
import time
from concurrent.futures import ThreadPoolExecutor

class BankAccount:
    def __init__(self, user_id, initial_balance):
        self.user_id = user_id
        self.balance = initial_balance
        self.lock = threading.Lock()  # Ensures thread safety

    def check_and_update(self, operation, amount):
        """Performs a thread-safe balance check and optional update."""
        with self.lock:
            # Simulate processing delay to increase context switch probability
            time.sleep(0.1) 
            
            if operation == "check":
                return f"User {self.user_id} balance: ${self.balance}"
            elif operation == "withdraw":
                if self.balance >= amount:
                    self.balance -= amount
                    return f"User {self.user_id} withdrew ${amount}. New balance: ${self.balance}"
                else:
                    return f"User {self.user_id} insufficient funds."
            elif operation == "deposit":
                self.balance += amount
                return f"User {self.user_id} deposited ${amount}. New balance: ${self.balance}"

def worker_task(account, operation, amount):
    """Wrapper function to execute tasks in the thread pool."""
    result = account.check_and_update(operation, amount)
    print(result)
    return result

def main():
    # Initialize three users with different starting balances
    users = [
        BankAccount(user_id=1, initial_balance=1000),
        BankAccount(user_id=2, initial_balance=500),
        BankAccount(user_id=3, initial_balance=2000)
    ]

    # Define tasks: 2 threads will handle these 3 operations concurrently
    # Tasks: Check balance for User 1, Withdraw from User 2, Deposit to User 3
    tasks = [
        (users[0], "check", 0),
        (users[1], "withdraw", 200),
        (users[2], "deposit", 500)
    ]

    # Use ThreadPoolExecutor with max_workers=2 to limit threads to 2
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the thread pool
        futures = [executor.submit(worker_task, *task) for task in tasks]
        
        # Wait for all tasks to complete and collect results
        for future in futures:
            future.result()

    # Print final balances after all threads finish
    print("\n--- Final Balances ---")
    for user in users:
        print(f"User {user.user_id}: ${user.balance}")

if __name__ == "__main__":
    main()   
