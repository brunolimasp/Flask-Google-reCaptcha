# Flask_Google_reCaptcha
---
## instalação

    pip install Flask_Google_reCaptcha


### Implemetação

    from flask import Flask
    from google_recaptcha_flask import ReCaptcha

    app = Flask(__name__)
    recaptcha = ReCaptcha(app)

    app.config.update(dict(
    GOOGLE_RECAPTCHA_ENABLED=True,
    GOOGLE_RECAPTCHA_SITE_KEY="SUA SITE CHAVE",
    GOOGLE_RECAPTCHA_SECRET_KEY="SUA CHAVE SECRETA"
))
recaptcha.init_app(app)
    
## Exemplo front-end
### Adicione no seu formulário : **{{ recaptcha }}**

    <form method="post" action="/submit">
        ...
        {{ recaptcha }}

        [submit]
    </form>


## Exemplo flask back-end
### validação de reCaptcha


    @route("/submit", methods=["POST"])
    def submit():

        if recaptcha.verify():
            print("SUCCESS") 
            
        else:
            print("FAILED")


## VARIÁVEIS

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""
    RECAPTCHA_THEME = "light"
    RECAPTCHA_TYPE = "image"
    RECAPTCHA_SIZE = "normal"
    RECAPTCHA_LANGUAGE = "pt-br"
    RECAPTCHA_RTABINDEX = 10


