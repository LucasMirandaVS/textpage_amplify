import json

def lambda_handler(event, context):
    # Extrai os dados diretamente do event
    nome = event.get('nome')
    nome_gotico = event.get('nome_gotico')
    
    # Verificação simples
    if not nome or not nome_gotico:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'status': 'erro',
                'mensagem': 'Campos "nome" e "nome_gotico" são obrigatorios.'
            })
        }

    # Retorna os dados informados com status de sucesso
    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'sucesso',
            'nome': nome,
            'nomeGotico': nome_gotico
        })
    }
