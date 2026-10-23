import gc

print(gc.isenabled())
gc.disable()  # To disable GC
print(gc.isenabled())
gc.enable()  # To enable GC
print(gc.isenabled())
