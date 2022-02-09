import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
from ritl import add, add_rel_imp
sys.path.pop(-1)

def main():
    try:
        from testdir.testscript import hello
        assert False
    except ModuleNotFoundError:
        assert True
    add(__file__, "../..")
    from testdir.testscript import hello
    assert hello() == "hello"
    sys.path.pop(-1)
    add_rel_imp("../..")
    from testdir.testscript import hello
    assert hello() == "hello"
    
if __name__ == "__main__":
    main()
    