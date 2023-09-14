name: Evaluering af produktniveau
description: OS2 arbejder med en tredelt governancemodel, der inddeler produkterne i tre niveauer ud fra organisatorisk og teknisk modenhedsniveau. 
body:
  - type: markdown
    attributes:
      value: |
        ## Relevans
        ### Løsningen skaber lokal værdi
        ### Løsningen skaber potentielt værdi for andre
        ### Løsningen er accepteret af lokal linjeledelse
        ### _Løsningen har tværkommunal potentiale (anbefaling)_
        ### Ophæng til nationale strategier er til stede
  - type: checkboxes
    id: checkbox1
    attributes:
      label: Bekræftelse af relevans for Niveau 1
      options:
        - label: Løsningen skal skabe lokal værdi.
        - label: Løsningen skal have potentiel værdi for andre.
  - type: input
    id: input1
    attributes:
      label: Hvordan skaber løsningen lokal værdi?
  - type: input
    id: input2
    attributes:
      label: Hvordan skaber løsningen potentielt værdi for andre?
  - type: input
    id: input3
    attributes:
      label: Hvordan er løsningen accepteret af lokal linjeledelse?
  - type: input
    id: input4
    attributes:
      label: Hvordan har løsningen tværkommunal potentiale (anbefaling)?
  - type: input
    id: input5
    attributes:
      label: Hvordan/hvilke ophæng til nationale strategier er til stede?
