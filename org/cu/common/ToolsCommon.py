import re
import time
import uuid

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Common method get current data
'''


def getCurrentDate(_format="%m/%d/%y") -> str:
    return time.strftime(_format, time.localtime())


'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Common method generate unique id
'''


def getId(_prefix="job-") -> str:
    return ((_prefix is None or len(_prefix) == 0) and uuid.uuid4()) or _prefix + (str(uuid.uuid4()))


'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Common method check whether None or len equal zero 
   @Note: the value must be can use method len() , like str,list,array .... ,Object can not use it.  
'''


def isNoneOrEmpty(value) -> bool:
    return value is None or len(value) == 0


'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/04/21
   @Common method check whether email
'''


def isEmail(value: str) -> bool:
    return not isNoneOrEmpty(value) and re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
                                                 value) is not None
