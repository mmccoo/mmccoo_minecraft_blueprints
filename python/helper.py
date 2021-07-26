
str = """                                        {{
                                            "origin": [-1032, {}, -1032],
					    "size": [2048, 1, 2048],
					    "uv": {{
					        "up": {{"uv": [{}, {}], "uv_size": [-128, -128]}}
					    }}
				        }},"""



# how high on a layer do we want the marker? 0-15
height = 8

filter = "all"

for y in range(100):
    if ((filter == "even") and (y%2) != 0):
        continue
    elif ((filter == "odd") and (y%2) != 1):
        continue

    x = 128*(int(y/10)+1)
    z = 128*((y%10)+1)

    # the positive layers start at 50.
    #print("y={}".format(y))
    print(str.format(height+(y-50)*16, x, z))
