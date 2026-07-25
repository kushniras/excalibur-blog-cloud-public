# Forbidden target sites — никогда не анализировать как «сайт клиента»

## Жёсткий запрет

Следующие домены **нельзя** использовать как целевой сайт для:

- GEO/SEO audit live site;
- Wave remaster / «доработка всех страниц»;
- baseline robots/llms/sitemap аудита «моего сайта»;
- publish/update контента «на мой сайт»;
- любых действий, где агент выбирает URL сайта сам, без явного `PUBLIC_SITE_URL` / brief клиента.

| Домен / бренд | Почему запрещён |
|---------------|-----------------|
| `mayai.ru` | Сайт **автора плагина** Excalibur BLOG (Maya AI / «Ковчег»). Не относится к сайтам клиента. |
| `www.mayai.ru` | То же. |
| Поддомены `*.mayai.ru` | То же, пока клиент явно не скажет иное. |

Синонимы в brief/артефактах, которые **не** делают mayai.ru целевым сайтом клиента: «Maya AI», «Ковчег», примеры URL в демо-статьях плагина.

## Откуда брать целевой сайт

1. Cloud Secrets / env: `PUBLIC_SITE_URL` (или `WP_SITE_URL` / `WP_HOME`) **клиента**.
2. Актуальный `memory/brief/site-brief.md` **только если** `site_url` совпадает с клиентским доменом из secrets / явной инструкции пользователя.
3. Если `site_url` в brief = `mayai.ru` или secrets пусты — **не** подставлять mayai.ru. Вернуть blocker:

```text
❌ TARGET SITE BLOCKER: mayai.ru — сайт автора плагина, не сайт клиента.
Задайте PUBLIC_SITE_URL (Cloud Secrets) и/или клиентский site-brief.site_url.
```

## Что можно

- Упоминать mayai.ru в **исторических** demo-артефактах репозитория как пример автора плагина.
- Читать локальные `memory/blog/articles/*` как шаблоны пайплайна **без** live crawl mayai.ru.
- Использовать mayai.ru **только** если пользователь явно написал: «это мой сайт / анализируй mayai.ru».

## Что нельзя

- `curl` / WP API / WebFetch аудита mayai.ru «по умолчанию».
- Remaster/publish на mayai.ru без явной команды владельца этого домена.
- Брать mayai.ru из site-brief как fallback, когда клиентский URL не задан.
