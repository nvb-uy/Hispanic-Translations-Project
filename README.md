# About
Hispanic Translations Project. An open source spanish translation project for Modded Minecraft.


Its purpose is to provide actively developed translations on the public domain for all Minecraft mods.
Any mod is free to use these translations, we encourage it and there's no need to credit.


The translations are uploaded in CurseForge or Modrinth as individiual resourcepacks by the HispanicTranslationsProject account.

## Disclaimer
Keep in mind that our translations are UNOFFICIAL. And they might have errors, if they do, we'd appreciate reports in the issues tab.


# Our goal
The goal of the Hispanic Translations Team is to provide a spanish translation for every modpack.


Not only adding missing translations, but also improving mods that either have missing keys (only x% of the mod is translated), or have certain issues we'd like to improve from our view.

# The Team

We are a small team of native spanish speakers

- ElocinDev (Founder, Proofreader and Translator)
- Askaban (Translator)

## Contributors

- [4drian](https://github.com/4drian) (Translator and Proofreader)
- KS_Debfyed (Translator and Proofreader)

# Building

To save time, the translation process is done in a single json file under src/translations, named just like the mod's id. Then, using the build.py you can create the resourcepacks.
It will clone the translations and put them in the respective files, then swap the slang words into their respective forms, like for example "Peto" and "Pechera" between different languages.

```python
python build.py
```

# Contributing

If the mod already exists, find its json file under src/translations.
If not, create a new json file with the mod's id as the name. Then add its translated entries.


Important, add the metadata entries if they don't exist, they're used by the build script when generating a resourcepack.
### Example Metadata Entries:
```json
"htp_metadata_version": "1.0.0",
"htp_metadata_credits": "This translation was made by the HTP (Hispanic Translations Projects) Team. \nTranslators: (Your Name)"
```

## Review Process
After doing a PR, you will be reviewed by approved moderators, and if needed, changes will be requested or made.


## Translation Rules
The general translation rules are:
- **Always think about what you'd like to see in-game.** The translation should be thought from the perspective of a native speaker user.

- **No aggressive translations.** Spanglish is more than welcome, not all text should be translated. Like unique names, such as the mod name, or items with names like "Thunderwrath" (DO NOT translate that to furia del trueno, please.)

## Slang
Default slang should be Spain's Spanish, the build script will handle slang differences and replace them, making it friendly for all countries.
For example, "Peto" should be the main word for chestplate, which will get replaced to "Pechera" within the build script in the specific countries that use it.
