const absolutePath = '/tester-a11y';
const titlePage = `Démo accessibilité numérique`;

window.onload = () => {
  getHtmlContent('components/main/main.html').then((innerHTML) => {
    document.querySelector('#app').innerHTML = innerHTML;
    loadComponents();
  });
};

function loadComponents() {
  customElements.define('router-outlet', RouterOutlet);
  customElements.define('router-link', RouterLink);
  customElements.define('custom-header', CustomHeader);
  customElements.define('custom-footer', CustomFooter);
  customElements.define('custom-picture', CustomPicture);
  customElements.define('custom-alert', CustomAlert);
}

class CustomHeader extends HTMLElement {
  async connectedCallback() {
    // loadStylesheet('components/header/header.scss');
    this.innerHTML = await getHtmlContent('components/header/header.html');

    this.initTheme();
    setAriaCurrentPage();
  }

  initTheme() {
    const themeStored = localStorage.getItem('theme');

    if (themeStored) {
      this.setTheme(themeStored);
    } else {
      if (
        window.matchMedia &&
        window.matchMedia('(prefers-color-scheme: dark)').matches
      ) {
        this.setTheme('dark');
      } else {
        this.setTheme('light');
      }
    }

    const btnLight = document.getElementById('btnLight');
    if (btnLight) {
      btnLight.onclick = () => this.setTheme('light');
    }

    const btnDark = document.getElementById('btnDark');
    if (btnDark) {
      btnDark.onclick = () => this.setTheme('dark');
    }
  }

  setTheme(theme) {
    var buttons = document.querySelectorAll('.theme-switcher-buttons button');
    buttons.forEach((button) => {
      const dataTheme = button.getAttribute('data-theme');
      if (dataTheme === theme) {
        button.setAttribute('aria-pressed', true);
      } else {
        button.setAttribute('aria-pressed', false);
      }
    });

    document.documentElement.setAttribute('data-selected-theme', theme);
    localStorage.setItem('theme', theme);
  }
}

class CustomFooter extends HTMLElement {
  async connectedCallback() {
    // loadStylesheet('components/footer/footer.scss');
    this.innerHTML = await getHtmlContent('components/footer/footer.html');
  }
}

class CustomPicture extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    let img = document.createElement('img');
    img.alt = this.attributes.alt.value;
    img.src = this.attributes.src.value;
    img.setAttribute('lazy', 'loading');

    if (this.attributes.style) {
      img.style = this.attributes.style.value;
    }

    if (this.attributes.class) {
      this.attributes.class.value.split(' ').forEach((value) => {
        img.classList.add(value);
      });
    }

    this.appendChild(img);
  }
}

class RouterOutlet extends HTMLElement {
  constructor() {
    super();
    window.addEventListener('popstate', () => this.handleRoute());
  }

  async connectedCallback() {
    await this.handleRoute();
  }

  async handleRoute() {
    const path = window.location.pathname.replace(absolutePath, '');

    let title = '';
    let filename = '';
    switch (path) {
      case '/':
        filename = 'pages/accueil.html';
        title = 'Accueil';
        break;
      case '/les-contrastes':
        filename = 'pages/les-contrastes.html';
        title = 'Testons les contrastes';
        break;
      case '/la-langue':
        filename = 'pages/cas-pratique-2.html';
        title = 'Testons la langue';
        break;
      case '/les-images':
        filename = 'pages/les-images.html';
        title = 'Les images';
        break;
      case '/les-formulaires':
        filename = 'pages/les-formulaires.html';
        title = 'Les formulaires';
        break;
      case '/cas-pratique-5':
        filename = 'pages/cas-pratique-5.html';
        title = 'Cas pratique n°5 : les liens';
        break;
      case '/cas-pratique-6':
        filename = 'pages/cas-pratique-6.html';
        title = 'Cas pratique n°6 : les boutons';
        break;
      case '/ci-cd':
        filename = 'pages/ci-cd.html';
        title = 'Tests automatisés';
        break;
      case '/bonus':
        filename = 'pages/bonus.html';
        title = 'Bonus';
        break;
      case '/faq':
        filename = 'pages/faq.html';
        title = 'Foire aux questions';
        break;
      case '/ressources':
        filename = 'pages/ressources.html';
        title = 'Ressources';
        break;
      case '/a-propos':
        filename = 'pages/a-propos.html';
        title = 'A propos';
        break;
      default:
        filename = 'pages/erreur.html';
        title = 'Erreur 404';
    }

    this.innerHTML = await getHtmlContent(filename);
    document.title = `${title} - ${titlePage}`;

    // Changer la langue de la page HTML selon la route
    if (path === '/la-langue') {
      document.documentElement.setAttribute('lang', 'en');
    } else {
      document.documentElement.setAttribute('lang', 'fr');
    }

    this.initJavascript(path);
    this.setCurrentPage(document.title);
  }

  setCurrentPage(title) {
    document.getElementById('title-page').innerHTML = title;
  }

  async navigate(path) {
    window.history.pushState({}, '', path);
    await this.handleRoute();
  }

  initJavascript(path) {
    if (path === '/les-images') {
      document
        .getElementById('show-button')
        .addEventListener('click', (event) => {
          displayPicture('.images');

          const element = event.target;

          const hasHidden = document.querySelector('.hidden') !== null;

          if (hasHidden) {
            element.innerText = 'Afficher les images';
          } else {
            element.innerText = 'Cacher les images';
          }
        });
    }

    if (path === '/les-formulaires') {
      // FORMULAIRE INACCESSIBLE : Uniquement bordure rouge, aucun message, aucun ARIA
      const btnBad = document.getElementById('btnSubmitBad');
      if (btnBad) {
        btnBad.addEventListener('click', () => {
          const form = document.getElementById('form-bad');
          const inputs = form.querySelectorAll('input');

          for (const input of inputs) {
            const hasValid = input.value.trim() !== '';

            if (!hasValid) {
              // Uniquement changement de bordure en rouge
              input.style.borderColor = 'red';
              input.style.borderWidth = '2px';
            } else {
              // Retirer la bordure rouge
              input.style.borderColor = '';
              input.style.borderWidth = '';
            }
          }
          // Pas d'alerte, pas de message d'erreur, pas d'ARIA
        });
      }

      // FORMULAIRE ACCESSIBLE : Implémentation complète DSFR avec tous les attributs ARIA
      const btnGood = document.getElementById('btnSubmitGood');
      if (btnGood) {
        btnGood.addEventListener('click', () => {
          const form = document.getElementById('form-good');
          const inputs = form.querySelectorAll('input');

          let hasSomeInputInvalid = false;

          for (const input of inputs) {
            // Validation basique : champ non vide
            let hasValid = input.value.trim() !== '';
            let errorMessage = '';

            // Validation spécifique pour l'email
            if (input.type === 'email' && hasValid) {
              const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
              hasValid = emailRegex.test(input.value);
              if (!hasValid) {
                errorMessage = 'Le format de l\'email est invalide (ex: nom@domaine.fr)';
              }
            }

            // Récupérer le groupe d'input DSFR et le message d'erreur
            const inputGroup = input.closest('.fr-input-group');
            const errorText = inputGroup.querySelector('.fr-error-text');
            const label = inputGroup.querySelector('.fr-label');

            if (hasValid) {
              // Champ valide : retirer les classes d'erreur DSFR
              input.classList.remove('fr-input--error');
              inputGroup.classList.remove('fr-input-group--error');
              input.ariaInvalid = false;
              errorText.innerText = '';
            } else {
              // Champ invalide : ajouter les classes d'erreur DSFR
              hasSomeInputInvalid = true;
              input.classList.add('fr-input--error');
              inputGroup.classList.add('fr-input-group--error');
              input.ariaInvalid = true;

              // Générer le message d'erreur
              if (errorMessage) {
                errorText.innerText = errorMessage;
              } else {
                // Extraire le texte du label (sans le hint-text et l'astérisque)
                const labelText = label.childNodes[0].textContent.trim();
                errorText.innerText = `Le champ ${labelText} est obligatoire`;
              }
            }
          }

          if (hasSomeInputInvalid) {
            displayAlert('error', 'Certains champs sont incomplets ou invalides !');

            // Donner le focus au premier champ invalide
            const element = document.querySelector('[aria-invalid=true]');
            if (element) {
              element.focus();
            }
          } else {
            displayAlert('success', 'Formulaire valide ! Tous les champs sont remplis correctement.');
          }
        });
      }
    }
  }
}

async function getHtmlContent(htmlFileName) {
  const responseHTML = await fetch(`${absolutePath}/${htmlFileName}`);
  if (!responseHTML.ok) {
    throw new Error(
      'Erreur lors du chargement du fichier HTML : ' + responseHTML.statusText
    );
  }

  return await responseHTML.text();
}

function loadStylesheet(url) {
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = `${absolutePath}/${url}`;

  document.head.appendChild(link);
}

function setAriaCurrentPage() {
  const routerLinks = document.querySelectorAll('router-link');

  routerLinks.forEach((routerLink) => {
    let link = routerLink.querySelector('a');

    const path = window.location.pathname.replace(absolutePath, '');

    if (path === routerLink.attributes.href.value) {
      link.setAttribute('aria-current', 'page');
      link.classList.add('active');
    } else {
      link.removeAttribute('aria-current');
      link.classList.remove('active');
    }

    link.addEventListener('click', () => {
      setAriaCurrentPage();
    });
  });
}

class RouterLink extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const link = document.createElement('a');

    const href = absolutePath + this.attributes.href.value;

    link.href = href;
    link.text = this.attributes.title.value;
    link.onclick = (event) => {
      event.preventDefault();
      document.querySelector('router-outlet').navigate(href);
    };

    this.appendChild(link);
  }
}

function displayPicture(selector) {
  const element = document.querySelector(selector);
  if (element) {
    if (element.classList.contains('hidden')) {
      element.classList.remove('hidden');
    } else {
      element.classList.add('hidden');
    }
  }
}

class CustomAlert extends HTMLElement {
  async connectedCallback() {
    loadStylesheet('components/alert/alert.scss');
    this.innerHTML = await getHtmlContent('components/alert/alert.html');
  }
}

function displayAlert(type, message) {
  let iconClassName = '';
  let className = '';

  switch (type) {
    case 'info':
      iconClassName = 'fa-circle-info';
      className = 'info';
      break;
    case 'success':
      iconClassName = 'fa-circle-check';
      className = 'success';
      break;
    case 'error':
      iconClassName = 'fa-circle-exclamation';
      className = 'error';
      break;
    default:
      return;
  }

  const alertElement = document.querySelector('.alert');
  if (!alertElement) {
    throw new Error("Le composant alert n'est pas défini");
  }

  alertElement.classList.add('display');
  alertElement.classList.add(className);

  const iconElement = alertElement.querySelector('i');
  if (iconElement) {
    iconElement.classList.add(iconClassName);
  }

  const alertMessageElement = alertElement.querySelector('.alert-title');
  if (alertMessageElement) {
    alertMessageElement.innerText = message;
  }

  const buttonElement = alertElement.querySelector('button');
  if (buttonElement) {
    buttonElement.addEventListener('click', () =>
      hideAlert(className, iconClassName)
    );
  }

  setTimeout(() => hideAlert(className, iconClassName), 1500);
}

function hideAlert(className, iconClassName) {
  const alertElement = document.querySelector('.alert');
  if (!alertElement) {
    throw new Error("Le composant alert n'est pas défini");
  }

  alertElement.classList.remove('display');
  alertElement.classList.remove(className);

  const iconElement = alertElement.querySelector('i');
  if (iconElement) {
    iconElement.classList.remove(iconClassName);
  }

  const alertMessageElement = alertElement.querySelector('.alert-title');
  if (alertMessageElement) {
    alertMessageElement.innerText = '';
  }

  const buttonElement = alertElement.querySelector('button');
  if (buttonElement) {
    buttonElement.removeEventListener('click', buttonElement);
  }
}
