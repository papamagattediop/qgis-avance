layer = iface.activeLayer()
classes = {}
for f in layer.getFeatures():
    c = f['classe']
    classes[c] = classes.get(c, 0) + 1

for c, n in classes.items():
    print(f"{c} : {n} polygones")