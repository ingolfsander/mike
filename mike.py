from flask import Flask, g, render_template

app = Flask(__name__)

@app.route("/ingolf/<action>/mike/")
def ingolf_mike(action):
    emotions = {
                'misses': 'deine neugier und dein wissen werden fehlen!',
                'loves': 'sei nicht so eingebildet!',
                'goes for lunch with': 'appetit auf pizza? schau doch mal wieder bei uns vorbei...!',
                'shirty': 'die problem ist...? hoer auf zu nerven! ;-)',
                'works with': 'die problem ist...? danke, dass du immer mitdenkst!',
               }
    return render_template('show_mike.html', message=emotions[action])

if __name__ == "__main__":
    app.debug = True
    app.run()

