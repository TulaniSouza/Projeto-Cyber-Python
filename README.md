# Simulador de Ransomware e Keylogger em Python

Este projeto foi desenvolvido como parte do desafio final da formação em **Cybersecurity** da **DIO**, com o objetivo de compreender a anatomia de ameaças cibernéticas para fortalecer estratégias de defesa.

## O que este projeto faz?

- **Criptografia Simétrica (Ransomware):** Utiliza a biblioteca `cryptography (Fernet)` para cifrar arquivos em um diretório de teste (`test_files`).
- **Recuperação de Dados (Decrypter):** Implementa a lógica reversa para restaurar os arquivos originais através de uma chave gerada localmente.
- **Monitoramento (Keylogger):** Captura teclas digitadas em tempo real (usando a biblioteca `pynput`) para demonstrar como dados sensíveis podem ser coletados por atacantes.

## Objetivo de Carreira
Abaixo, um exemplo da recuperação de um arquivo de imagem crítico após o processo de descriptografia:

![Contratação](./test_files/image.jpg)

*Este projeto demonstra não apenas habilidades técnicas em Python e Segurança, mas também a capacidade de utilizar IAs generativas para criar contextos de teste e materiais de portfólio.*

## Boas Práticas de Segurança Aplicadas
- **Secrets Management:** O arquivo de chave (`chave.key`) e os logs (`log_teclado.txt`) foram incluídos no `.gitignore` para evitar o vazamento de informações sensíveis no repositório.
- **Security by Design:** O código foi estruturado para atuar apenas em pastas controladas de teste.

## Aviso Legal
Este software foi criado estritamente para fins educacionais. O uso destas técnicas em ambientes sem autorização expressa é ilegal e viola os princípios da ética hacker.
