# A small tool to configure our Arduinos
**Main logic:**

1. Check if Arduino is connected and attempt to start
1.1. If it isn't, throw a error and exit
2. Read Arduino's parameters
2.1. If some of parameters are impossible to read or incorrect, display NaN
3. Display mainwindow and allow a user to choose parameters
3.1. User is allowed to choose between presets
		3.1.1. One of presets is revert, it makes things on Arduino the same they were before this tool started
		3.1.2. Another are some default presets, designed for different rooms and acoustic conditions
4. Save settings
4.1. If user didn't fixed NaN parameters, throw a error
4.2. If Arduino has been disconnected, throw a error 

**Done for now:**
nothing, only a layout is partially done, just for understanding how it should look like

**To-do:**
everything
