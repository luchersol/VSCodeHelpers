MethodHandles.Lookup lookup = MethodHandles.lookup();
MethodHandle mh = lookup.findVirtual(MyClass.class, "methodName",
    MethodType.methodType(int, ptype0, ptype1, ...);

MyClass obj = new MyClass();
int result = (int) mh.invoke(obj, ptype0, ptype1, ...);