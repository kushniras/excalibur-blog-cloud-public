# GEO remaster queue — ARCHIVED (wrong target)

`created`: 2026-07-25  
`status`: **superseded / wrong target**  
`rules`: shared/geo-collider-remediation-rules.md  
`audit`: memory/blog/geo-site-audit-2026-07-25.json  

> **⚠ Ошибка scope:** этот queue/audit относится к `mayai.ru` — сайту **автора плагина**, не к сайтам клиента.  
> **Никогда не продолжать** live remaster/publish на mayai.ru.  
> Канон: `shared/forbidden-target-sites.md`. Новый remaster — только после клиентского `PUBLIC_SITE_URL` + своего brief.

`llms_txt_urls`: 84  
`site_posts_total`: 5122  
`site_pages_total`: 232  
`target_was`: https://mayai.ru *(FORBIDDEN)*

## Волны

| Волна | Scope | Статус |
|-------|-------|--------|
| A | Technical foundation (robots AI bots, sitemap) | mostly done on live |
| B | 84 URL из llms.txt + local B01–B10 | remastered_local done |
| C | Thin/scaled tail (score≤2) | queued — editor decision, no auto-delete |
| D | Multi-engine measurement baseline | after B |

## Wave B — priority order (higher weight first)

| # | weight | score | local | modified | slug | gaps | status |
|---|--------|-------|-------|----------|------|------|--------|
| 1 | 60 | 6 | B05 | 2026-07-25 | `avtonomnyj-kontent-zavod-nejroseti` | lead, updated, tldr_antipattern | remastered_local |
| 2 | 60 | 9 | B04 | 2026-07-25 | `geo-optimizaciya-sajta-2026` | tldr_antipattern | remastered_local |
| 3 | 60 | 9 | B09 | 2026-07-25 | `sozdat-llms-txt-dlya-sajta` | tldr_antipattern | remastered_local |
| 4 | 53 | 7 | B06 | 2026-07-25 | `make-ai-agents-mcp-avtomatizaciya` | table, updated, tldr_antipattern | remastered_local |
| 5 | 45 | 8 | B02 | 2026-07-25 | `avtomatizaciya-n8n-ai-agents` | updated, tldr_antipattern | remastered_local |
| 6 | 45 | 8 | B08 | 2026-07-25 | `ii-chat-bot-dlya-biznesa-workflow` | updated, tldr_antipattern | remastered_local |
| 7 | 45 | 8 | B03 | 2026-07-25 | `podklyuchenie-mcp-cursor` | updated, tldr_antipattern | remastered_local |
| 8 | 43 | 8 | R-mikro | 2026-07-25 | `mikrorazmetka-sajta-json-ld` | table, updated | remastered_local |
| 9 | 35 | 9 | R-indexnow | 2026-07-25 | `indexnow-yandex-make` | updated | remastered_local |
| 10 | 35 | 9 | B10 | 2026-07-25 | `ollama-lokalnaya-llm-dlya-biznesa` | tldr_antipattern | remastered_local |
| 11 | 35 | 9 | B07 | 2026-07-25 | `postroenie-rag-sistemy-vektornaya-baza` | tldr_antipattern | remastered_local |
| 12 | 35 | 9 | R-semyadro | 2026-07-25 | `semanticheskoe-yadro-cursor-wordstat` | updated | remastered_local |
| 13 | 35 | 9 | R-seoaudit | 2026-07-25 | `seo-audit-sajta-cursor-geo-skill` | updated | remastered_local |
| 14 | 35 | 9 | R-perelink | 2026-07-25 | `vnutrennyaya-perelinkovka-statej-kontent-zavod` | updated | remastered_local |
| 15 | 30 | 7 | R-avtopost-tg | 2026-07-25 | `kak-nastroit-avtoposting-telegram-cloud-agents` | steps, table, updated | remastered_local |
| 16 | 30 | 7 | R-limity | 2026-07-25 | `kak-proverit-limity-cursor-pered-agentami` | steps, table, updated | remastered_local |
| 17 | 30 | 7 | R-aura | 2026-07-25 | `kak-ustanovit-aura-dizajn-subagent-cursor` | steps, table, updated | remastered_local |
| 18 | 25 | 10 | R-alisa | 2026-07-25 | `prodvizhenie-v-nejrosetyah-alisa-checklist` | ok | remastered_local |
| 19 | 18 | 8 | R-webhook | 2026-07-25 | `kak-nastroit-cursor-automations-po-webhook` | table, updated | remastered_local |
| 20 | 18 | 8 | R-ruleset | 2026-07-25 | `kak-nastroit-ruleset-i-skill-cursor` | table, updated | remastered_local |
| 21 | 18 | 8 | R-mcp-sub | 2026-07-25 | `kak-podklyuchit-mcp-subagentam-cursor` | table, updated | remastered_local |
| 22 | 18 | 8 | R-bg-remove | 2026-07-25 | `kak-udalit-fon-nejrosetyu-mcp-cursor` | table, updated | remastered_local |
| 23 | 18 | 8 | R-sdk | 2026-07-25 | `kak-zapustit-lokalnyy-ai-agent-cursor-sdk` | table, updated | remastered_local |
| 24 | 18 | 8 | R-og | 2026-07-25 | `open-graph-sait-cursor-ai` | table, updated | remastered_local |
| 25 | 18 | 8 | R-roli | 2026-07-25 | `roli-subagentov-cursor-orchestrator` | table, updated | remastered_local |
| 26 | 18 | 8 | R-yadisk | 2026-07-25 | `yandeks-disk-api-make-kontent-zavod` | table, updated | remastered_local |
| 27 | 12 | 9 | R-karuselka | 2026-07-25 | `kak-ustanovit-karuselka-instagram-subagent-cursor` | steps | remastered_local |
| 28 | 12 | 9 | R-yadryshko | 2026-07-25 | `kak-ustanovit-yadryshko-seo-subagent-cursor` | steps | remastered_local |
| 29 | 10 | 9 | R-ai-mkt | 2026-07-25 | `ai-agent-marketing-cursor-subagents` | updated | remastered_local |
| 30 | 10 | 9 | R-avtootvet | 2026-07-25 | `avtootvetchik-telegram-make` | updated | remastered_local |
| 31 | 10 | 9 | R-lending | 2026-07-25 | `cursor-ai-lending-bez-koda` | updated | remastered_local |
| 32 | 10 | 9 | R-cloud-ag | 2026-07-25 | `cursor-cloud-agents-avtomatizaciya` | updated | remastered_local |
| 33 | 10 | 9 | R-composer | 2026-07-25 | `cursor-composer-dlya-marketinga` | updated | remastered_local |
| 34 | 10 | 9 | R-ekonomika | 2026-07-25 | `cursor-ekonomika-ai-agentov` | updated | remastered_local |
| 35 | 10 | 9 | R-skills | 2026-07-25 | `cursor-skills-dlya-marketinga` | updated | remastered_local |
| 36 | 10 | 9 | R-design-md | 2026-07-25 | `design-md-cursor-ai` | updated | remastered_local |
| 37 | 10 | 9 | R-parallax | 2026-07-25 | `effekt-parallaksa-hero-cursor` | updated | remastered_local |
| 38 | 10 | 9 | R-favicon | 2026-07-25 | `favicon-sait-cursor-ai` | updated | remastered_local |
| 39 | 10 | 9 | R-gen-img | 2026-07-25 | `generaciya-kartinok-mcp-cursor-marketing` | updated | remastered_local |
| 40 | 10 | 9 | R-schedule | 2026-07-25 | `kak-nastroit-cursor-automations-po-raspisaniyu` | updated | remastered_local |
| 41 | 10 | 9 | R-prompts | 2026-07-25 | `kak-pisat-promty-dlya-nejroseti-cursor` | updated | remastered_local |
| 42 | 10 | 9 | R-context | 2026-07-25 | `kak-sohranit-kontekst-subagentov-cursor` | updated | remastered_local |
| 43 | 10 | 9 | R-ofis | 2026-07-25 | `kak-ustanovit-ofis-veb-stranits-cursor` | updated | remastered_local |
| 44 | 10 | 9 | R-vybrat | 2026-07-25 | `kak-vybrat-cloud-agents-automations-sdk-cursor` | updated | remastered_local |
| 45 | 10 | 9 | R-karusel | 2026-07-25 | `karusel-instagram-nejroseti-cursor` | updated | remastered_local |
| 46 | 10 | 9 | R-kviz | 2026-07-25 | `kviz-lidov-make-telegram` | updated | remastered_local |
| 47 | 10 | 9 | R-lido | 2026-07-25 | `lidogeneraciya-make-telegram-cursor` | updated | remastered_local |
| 48 | 10 | 9 | R-mudbord | 2026-07-25 | `mudbord-nejroset-cursor-marketing` | updated | remastered_local |
| 49 | 10 | 9 | R-statya | 2026-07-25 | `napisat-statyu-nejrosetyu-cursor` | updated | remastered_local |
| 50 | 10 | 9 | R-reklama | 2026-07-25 | `nejroset-dlya-reklamy-cursor` | updated | remastered_local |
| 51 | 10 | 9 | R-video | 2026-07-25 | `nejroset-dlya-sozdaniya-video-make-cursor` | updated | remastered_local |
| 52 | 10 | 9 | R-montazh | 2026-07-25 | `nejroset-montazh-video-reels-cursor` | updated | remastered_local |
| 53 | 10 | 9 | R-oblozhka | 2026-07-25 | `oblozhka-dlya-posta-nejroset-mcp` | updated | remastered_local |
| 54 | 10 | 9 | R-opisanie | 2026-07-25 | `opisanie-tovara-nejroset-cursor` | updated | remastered_local |
| 55 | 10 | 9 | R-pereobhod | 2026-07-25 | `pereobhod-stranic-yandeks-vebmaster-make` | updated | remastered_local |
| 56 | 10 | 9 | R-plaginy | 2026-07-25 | `plaginy-cursor-ai-marketing` | updated | remastered_local |
| 57 | 10 | 9 | R-podbor | 2026-07-25 | `podbor-klyuchevyh-slov-cursor-wordstat` | updated | remastered_local |
| 58 | 10 | 9 | R-progrev | 2026-07-25 | `progrev-akkauntov-pered-avtopostingom` | updated | remastered_local |
| 59 | 10 | 9 | R-rassylka | 2026-07-25 | `rassylka-telegram-make-google-sheets` | updated | remastered_local |
| 60 | 10 | 9 | R-scenarij | 2026-07-25 | `scenarij-reels-nejroset-cursor` | updated | remastered_local |
| 61 | 10 | 9 | R-404 | 2026-07-25 | `stranica-404-cursor-ai` | updated | remastered_local |
| 62 | 10 | 9 | R-faq-page | 2026-07-25 | `stranica-faq-cursor-ai` | updated | remastered_local |
| 63 | 10 | 9 | R-otzyvy | 2026-07-25 | `stranica-otzyvov-cursor-ai` | updated | remastered_local |
| 64 | 10 | 9 | R-portfolio | 2026-07-25 | `stranica-portfolio-cursor-ai` | updated | remastered_local |
| 65 | 10 | 9 | R-miniapp | 2026-07-25 | `telegram-mini-app-cursor-ai` | updated | remastered_local |
| 66 | 10 | 9 | R-openclaw | 2026-07-25 | `ustanovka-openclaw-make-cursor` | updated | remastered_local |
| 67 | 10 | 9 | R-vajb | 2026-07-25 | `vajbkoding-marketing-cursor-ai` | updated | remastered_local |
| 68 | 10 | 9 | R-webhook-make | 2026-07-25 | `webhook-make-pervyj-scenarij` | updated | remastered_local |
| 69 | 10 | 9 | R-wordstat-api | 2026-07-25 | `wordstat-api-make-google-sheets` | updated | remastered_local |
| 70 | 10 | 9 | R-karta | 2026-07-25 | `yandeks-karta-sait-cursor-ai` | updated | remastered_local |
| 71 | 10 | 9 | R-metrika | 2026-07-25 | `yandeks-metrika-api-cursor-skill` | updated | remastered_local |
| 72 | 8 | 9 | R-threads | 2026-07-25 | `avtoposting-threads-make-google-sheets` | table | remastered_local |
| 73 | 8 | 9 | R-giperion | 2026-07-25 | `kak-ustanovit-giperion-reels-subagent-cursor` | table | remastered_local |
| 74 | 8 | 9 | R-teya | 2026-07-25 | `mnogostranichnyj-sait-cursor-teya` | table | remastered_local |
| 75 | 5 | 0 | B01 | 2026-07-25 | `primer-seo-stati` | unknown | remastered_local |
| 76 | 0 | 10 | R-avtomark | 2026-07-25 | `avtomatizaciya-marketinga-make-cursor` | ok | remastered_local |
| 77 | 0 | 10 | R-bot-zayavok | 2026-07-25 | `bot-dlya-zayavok-telegram-make` | ok | remastered_local |
| 78 | 0 | 10 | R-cookie | 2026-07-25 | `cookie-banner-sait-cursor-ai` | ok | remastered_local |
| 79 | 0 | 10 | R-junior | 2026-07-25 | `kak-ustanovit-cursor-junior-nastavnik` | ok | remastered_local |
| 80 | 0 | 10 | R-excalibur | 2026-07-25 | `kak-ustanovit-excalibur-avtoblog-cursor` | ok | remastered_local |
| 81 | 0 | 10 | R-make-n8n | 2026-07-25 | `make-ili-n8n-dlya-marketinga` | ok | remastered_local |
| 82 | 0 | 10 | R-otlozh | 2026-07-25 | `otlozhennyj-posting-make-google-sheets` | ok | remastered_local |
| 83 | 0 | 10 | R-about | 2026-07-25 | `stranica-o-kompanii-cursor-ai` | ok | remastered_local |
| 84 | 0 | 10 | R-tilda | 2026-07-25 | `tilda-ai-agent-potoki-nejroset` | ok | remastered_local |

## Wave C — thin sample (no auto-delete)

| chars | modified | slug |
|------:|----------|------|
| 16 | 2025-09-08 | `proverka-novogo-podklyucheniya-4` |
| 16 | 2025-09-08 | `proverka-novogo-podklyucheniya-3` |
| 16 | 2025-09-08 | `proverka-novogo-podklyucheniya-2` |
| 16 | 2025-09-08 | `proverka-novogo-podklyucheniya` |
| 32 | 2025-09-29 | `obnovlennaya-testovaya-statya` |
| 197 | 2025-10-05 | `mcp-server-not-authenticated` |
| 405 | 2025-03-06 | `kak-sdelat-rabochie-proczessy-effektivnee-s-make-com-i-nejrosetyami-sekrety-uspeha-i-prostye-shagi-dlya-starta-uzhe-segodnya` |
| 423 | 2025-02-12 | `kak-avtomatizirovat-rabochie-proczessy-s-make-com-i-nejrosetyami-dlya-maksimalnoj-produktivnosti-i-rosta-biznesa` |
| 423 | 2025-01-15 | `avtomatizacziya-biznes-proczessov-s-make-com-i-nejrosetyami-otkrojte-novye-gorizonty-dlya-uspeha-vashej-kompanii` |
| 423 | 2024-12-27 | `avtomatizacziya-biznesa-kak-make-com-i-nejroseti-pomogut-vam-dostich-maksimalnoj-effektivnosti` |
| 426 | 2024-12-19 | `avtomatizacziya-biznes-proczessov-s-make-com-i-nejrosetyami-7-shagov-k-povysheniyu-effektivnosti-raboty-vashego-predpriyatiya` |
| 429 | 2025-02-13 | `avtomatizacziya-rabochih-proczessov-dlya-novichkov-poshagovoe-rukovodstvo-s-make-com-i-nejrosetyami` |
| 429 | 2025-01-29 | `osvobodite-vremya-i-uvelichte-produktivnost-kak-sdelat-avtoposting-s-make-com-legko-i-effektivno` |
| 429 | 2025-01-28 | `avtomatizacziya-rabochih-proczessov-effektivnye-sovety-po-ispolzovaniyu-make-com-i-nejrosetej-dlya-povysheniya-produktivnosti` |
| 716 | 2025-10-16 | `kupit-avtovoronku-v-telegram-nastrojka-pod-klyuch` |
| 1627 | 2026-01-24 | `kurs-po-integraczii-vkontakte-i-make-com-avto` |
| 1681 | 2025-10-28 | `hotite-uprostit-obshhenie-v-vk-uznajte-kak-avtomatizacziya-kommentariev-pomozhet-vam-upravlyat-otvetami-skryvat-spam-i-sozdavat-faq` |
| 2008 | 2025-10-28 | `ne-znaete-kak-otslezhivat-status-zakaza-v-internet-magazine-cherez-vk-uznajte-kak-nastroit-uvedomleniya-v-ls-i-byt-v-kurse` |
| 2413 | 2025-10-28 | `hotite-prodvinut-svoj-biznes-v-vkontakte-uznajte-kak-sozdat-dinamicheskie-vitriny-i-katalog-tovarov-v-soobshhestve` |
| 2487 | 2025-10-28 | `zadumyvalis-o-povtornyh-prodazhah-uznajte-kak-retargeting-v-vk-pomozhet-vernut-klientov-i-uvelichit-konversii` |
| 2947 | 2025-12-26 | `messendzher-max-novyj-goluboj-okean-dlya-biznesa-v-rf-i-avtomatizacziya-cherez-make-com` |
| 3102 | 2024-09-15 | `sozdanie-subtitrov-k-video-s-pomoshhyu-yandex-s` |
| 3328 | 2024-09-16 | `ispolzovanie-tinkoff-voicekit-dlya-golosovoj-biome` |
| 3447 | 2024-10-04 | `make-com-academy-polnoe-rukovodstvo-po-obucheniyu-i-s` |
| 3449 | 2024-09-12 | `kak-analizirovat-finansovye-dannye` |
| 3486 | 2024-09-12 | `rukovodstvo-po-sozdaniyu-logotipov-v-looka` |
