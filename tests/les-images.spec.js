// @ts-check
import { test, expect } from '@playwright/test';

test.describe('les-images', () => {
  test('Est-ce que les images de ce site sont accessibles ?', async ({
    page,
  }) => {
    await page.goto('./les-images');

    // Vérifier que la page se charge correctement
    await expect(page.locator('h1')).toContainText('Testons les images');

    // Vérifier la présence de la question d'accroche
    const callout = page.locator('.fr-callout').first();
    await expect(callout).toBeVisible();

    // Vérifier la présence des sections principales
    const exemplesTitre = page.locator('h2', { hasText: 'Exemples : avant / après' });
    await expect(exemplesTitre).toBeVisible();

    const criteresTitre = page.locator('h2', { hasText: 'Bonnes pratiques et critères RGAA' });
    await expect(criteresTitre).toBeVisible();

    const correctionTitre = page.locator('h2', { hasText: 'Comment corriger ?' });
    await expect(correctionTitre).toBeVisible();

    // Vérifier la présence des badges conforme/non conforme
    const badgesError = page.locator('.fr-badge--error');
    const badgesSuccess = page.locator('.fr-badge--success');

    await expect(badgesError.first()).toBeVisible();
    await expect(badgesSuccess.first()).toBeVisible();

    // Vérifier que les 9 critères RGAA sont présents
    const critere1_1 = page.locator('h4', { hasText: 'Critère 1.1' });
    const critere1_9 = page.locator('h4', { hasText: 'Critère 1.9' });

    await expect(critere1_1).toBeVisible();
    await expect(critere1_9).toBeVisible();
  });
});
