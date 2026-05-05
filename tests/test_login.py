import sys 
sys.path.insert(0, '.') 
from app import login 
 
def test_login_sukses(): 
    assert login("admin", "1234") == True 
 
def test_login_gagal(): 
    assert login("user", "wrong") == False 
