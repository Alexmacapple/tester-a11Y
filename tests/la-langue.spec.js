// @ts-check
import { test, expect } from '@playwright/test';

test.describe('la-langue', () => {
  test('Est-ce que ce site est vocalisable dans la bonne langue ?', async ({
    page,
  }) => {
    await page.goto('./la-langue');

    const lang = await page.getAttribute('html', 'lang');

    await expect(lang).toBe('fr');
  });
});
