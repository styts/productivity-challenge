# Productivity Challenge Helper

The android app is available [here](https://play.google.com/store/apps/details?id=com.wlxd.pomochallenge&hl=en).

Use the *backup* feature of the app to create a backup file (`*.pctb`) and copy
it from the sdcard to `backup.json` in directory of the app.

Running `python main.py` should will read `backup.json` and create
`output.xlsx` with daily work statistics per project.

You may need to `pip install xlsxwriter` to install the Excel file writing library.
The program uses `python3`.

It's just a very basic sketch for my use case so far, you may need to adapt a
few things yourself. If you can't figure it out, let me know - I'll try to help.
