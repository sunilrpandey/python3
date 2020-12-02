from derived import Derived


class TestBaseImpl:
    """
    this class demos calling base class impl of given object which is initialized
    with derived class
    """

    __der_ob = None

    def __init__(self):
        self.__der_ob = Derived()

    def call_base_impl_of_obj(self):
        super(self.__der_ob.__class__, self.__der_ob).fun_impl()
        # self.__ob.fun_impl()
        # self.__ob.common_fun()


def demo_call_base_impl():
    bimpl = TestBaseImpl()
    bimpl.call_base_impl_of_obj()


if __name__ == "__main__":
    demo_call_base_impl()
