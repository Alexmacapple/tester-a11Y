// @ts-check
import { test, expect } from '@playwright/test';

test.describe('les-formulaires', () => {
  test('Est-ce que la page se charge correctement ?', async ({ page }) => {
    await page.goto('./les-formulaires');

    // Vérifier que la page se charge correctement
    await expect(page.locator('h1')).toContainText('Testons les formulaires');

    // Vérifier la présence de la question d'accroche
    const callout = page.locator('.fr-callout').first();
    await expect(callout).toBeVisible();

    // Vérifier la présence des sections principales
    const experimenterTitre = page.locator('h2', {
      hasText: 'Expérimentez le problème',
    });
    await expect(experimenterTitre).toBeVisible();

    const tableauTitre = page.locator('h2', {
      hasText: 'Tableau comparatif des 4 versions',
    });
    await expect(tableauTitre).toBeVisible();

    const testezTitre = page.locator('h2', {
      hasText: 'Testez par vous-même',
    });
    await expect(testezTitre).toBeVisible();

    const criteresTitre = page.locator('h2', {
      hasText: 'Bonnes pratiques et critères RGAA',
    });
    await expect(criteresTitre).toBeVisible();

    // Vérifier la présence des 4 formulaires
    const formV1 = page.locator('#form-v1');
    const formV2 = page.locator('#form-v2');
    const formV3 = page.locator('#form-v3');
    const formV4 = page.locator('#form-v4');

    await expect(formV1).toBeVisible();
    await expect(formV2).toBeVisible();
    await expect(formV3).toBeVisible();
    await expect(formV4).toBeVisible();

    // Vérifier les badges
    const badgeError = page.locator('.fr-badge--error');
    const badgeWarning = page.locator('.fr-badge--warning');
    const badgeSuccess = page.locator('.fr-badge--success');

    await expect(badgeError.first()).toBeVisible();
    await expect(badgeWarning.first()).toBeVisible();
    await expect(badgeSuccess.first()).toBeVisible();

    // Vérifier le tableau comparatif
    const table = page.locator('.fr-table table');
    await expect(table).toBeVisible();
  });

  test('Version 1 - Uniquement couleur (non conforme)', async ({ page }) => {
    await page.goto('./les-formulaires');

    const formV1 = page.locator('#form-v1');
    const btnSubmitV1 = page.locator('#btnSubmitV1');

    // Vérifier que le formulaire est visible
    await expect(formV1).toBeVisible();
    await expect(btnSubmitV1).toBeVisible();

    // Soumettre le formulaire vide
    await btnSubmitV1.click();

    // Vérifier que les champs ont une bordure rouge (style inline)
    const inputV1Nom = page.locator('#v1-nom');
    const borderColor = await inputV1Nom.evaluate((el) => el.style.borderColor);
    expect(borderColor).toBe('red');

    // Pas d'aria-invalid dans V1
    const ariaInvalid = await inputV1Nom.getAttribute('aria-invalid');
    expect(ariaInvalid).toBeNull();
  });

  test('Version 2 - Labels associés (partiellement conforme)', async ({ page }) => {
    await page.goto('./les-formulaires');

    const formV2 = page.locator('#form-v2');
    const btnSubmitV2 = page.locator('#btnSubmitV2');

    // Vérifier que le formulaire est visible
    await expect(formV2).toBeVisible();

    // Vérifier que les labels ont l'attribut for
    const labelNom = page.locator('label[for="v2-nom"]');
    await expect(labelNom).toBeVisible();

    // Soumettre le formulaire vide
    await btnSubmitV2.click();

    // Vérifier que les champs ont une bordure rouge
    const inputV2Nom = page.locator('#v2-nom');
    const borderColor = await inputV2Nom.evaluate((el) => el.style.borderColor);
    expect(borderColor).toBe('red');

    // Vérifier que required est présent
    await expect(inputV2Nom).toHaveAttribute('required');
  });

  test('Version 3 - Messages d\'erreur (partiellement conforme)', async ({ page }) => {
    await page.goto('./les-formulaires');

    const formV3 = page.locator('#form-v3');
    const btnSubmitV3 = page.locator('#btnSubmitV3');

    // Vérifier que le formulaire est visible
    await expect(formV3).toBeVisible();

    // Soumettre le formulaire vide
    await btnSubmitV3.click();

    // Vérifier qu'un message d'erreur est affiché
    const errorText = page.locator('#error-v3-nom');
    await expect(errorText).toContainText('obligatoire');

    // Vérifier que les classes DSFR sont ajoutées
    const inputV3Nom = page.locator('#v3-nom');
    await expect(inputV3Nom).toHaveClass(/fr-input--error/);

    // Vérifier que aria-describedby est présent
    await expect(inputV3Nom).toHaveAttribute('aria-describedby', 'error-v3-nom');

    // Pas d'aria-invalid dans V3 (volontairement)
    const ariaInvalid = await inputV3Nom.getAttribute('aria-invalid');
    expect(ariaInvalid).toBeNull();
  });

  test('Version 4 - Formulaire complet (conforme)', async ({ page }) => {
    await page.goto('./les-formulaires');

    const formV4 = page.locator('#form-v4');
    const btnSubmit = page.locator('#btnSubmit');

    // Vérifier que le formulaire est visible
    await expect(formV4).toBeVisible();

    // Vérifier la présence des 4 champs
    const inputPrenom = page.locator('#txtPrenom');
    const inputNom = page.locator('#txtNom');
    const inputEmail = page.locator('#txtMail');
    const textareaMessage = page.locator('#txtMessage');

    await expect(inputPrenom).toBeVisible();
    await expect(inputNom).toBeVisible();
    await expect(inputEmail).toBeVisible();
    await expect(textareaMessage).toBeVisible();

    // Vérifier que les champs ont aria-required
    await expect(inputPrenom).toHaveAttribute('aria-required', 'true');
    await expect(inputNom).toHaveAttribute('aria-required', 'true');
    await expect(inputEmail).toHaveAttribute('aria-required', 'true');
    await expect(textareaMessage).toHaveAttribute('aria-required', 'true');

    // Essayer de soumettre le formulaire vide
    await btnSubmit.click();

    // Vérifier que les champs sont marqués comme invalides
    await expect(inputPrenom).toHaveAttribute('aria-invalid', 'true');

    // Vérifier qu'une alerte d'erreur est affichée
    const alert = page.locator('.alert.error');
    await expect(alert).toBeVisible();

    // Remplir tous les champs correctement
    await inputPrenom.fill('Jean');
    await inputNom.fill('Dupont');
    await inputEmail.fill('jean.dupont@example.com');
    await textareaMessage.fill('Ceci est un message de test');

    // Soumettre le formulaire
    await btnSubmit.click();

    // Vérifier que les champs sont marqués comme valides
    await expect(inputPrenom).toHaveAttribute('aria-invalid', 'false');

    // Vérifier qu'une alerte de succès est affichée
    const alertSuccess = page.locator('.alert.success');
    await expect(alertSuccess).toBeVisible();
  });

  test('Vérifier les critères RGAA', async ({ page }) => {
    await page.goto('./les-formulaires');

    // Vérifier que les critères RGAA sont présents (utiliser des sélecteurs plus précis)
    const critere11_1 = page.locator('h4', { hasText: 'Critère 11.1 - Présence' });
    const critere11_2 = page.locator('h4', { hasText: 'Critère 11.2 - Pertinence' });
    const critere11_9 = page.locator('h4', { hasText: 'Critère 11.9 - Pertinence des boutons' });
    const critere11_10 = page.locator('h4', { hasText: 'Critère 11.10 - Identification' });

    await expect(critere11_1).toBeVisible();
    await expect(critere11_2).toBeVisible();
    await expect(critere11_9).toBeVisible();
    await expect(critere11_10).toBeVisible();
  });
});
