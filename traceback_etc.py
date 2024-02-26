import traceback

def tracebackfunctnion():
  try:
    print("정상 작동 전")
    0/0
    print("오류")

  except Exception as ex:
    print("오류 메세지 출력")
    err_msg = traceback.format_exc()

    print("err_msg" , err_msg)


tracebackfunctnion()