# Teste de Sistema Web com Selenium - Introdução
Prof. Andre Hora

Objetivo: exercitar Testes de Sistema Web, com o framework Selenium.

Abra o arquivo `test_google_query.py` e explore o código. Após, clique no botão **run** e veja o teste web sendo executado com sucesso no terminal à direita.
Observe que o navegador (Chrome nesse caso) será aberto e o script de teste será executado no navegador.

Após executar o teste, implemente no método `test_can_query_on_google` mais 3 asserts.
Veja que já existe um `self.assertIn(...)` que testa o `title` da página, conforme abaixo:

```python
self.assertIn("software testing", self.driver.title)
# todo: assert 1
# todo: assert 2
# todo: assert 3
```

Você deve estudar a [documentação do Selenium](https://selenium-python.readthedocs.io/api.html) para saber o que testar. Por exemplo, você pode utilizar/testar o `page_source`, `current_url`, etc.