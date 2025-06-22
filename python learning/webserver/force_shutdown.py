import subprocess
import time


def countdown_shutdown(countdown_time):
    try:
        # 倒计时
        for i in range(countdown_time, 0, -1):
            time.sleep(1)

        # 调用系统关机命令
        subprocess.run(["shutdown", "/s", "/f", "/t", "0"], check=True)
        print("Shutdown command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute shutdown command: {e}")


if __name__ == "__main__":
    try:
        countdown_time = int(input("Enter countdown time in seconds: "))  # 用户输入倒计时时间
        countdown_shutdown(countdown_time)
    except ValueError:
        print("Invalid input. Please enter an integer.")
