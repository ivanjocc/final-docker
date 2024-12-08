import requests

class AIAssistantChatbot:
    def __init__(self, base_url="http://localhost:11434"):
        """
        Initialise l'assistant avec Ollama exécuté localement.
        """
        self.base_url = base_url
        self.context = []

    def generate_response(self, user_message, user_role='candidate'):
        """
        Génération de réponses contextuelles avec Ollama.
        """
        # Ajouter le message utilisateur au contexte
        self.context.append({"role": "user", "content": user_message})

        # Définir le prompt initial pour Ollama
        system_prompt = (
            "Tu es un assistant IA spécialisé dans le recrutement. "
            "Aide les candidats et recruteurs avec des conseils professionnels."
        )

        # Construire le payload pour la requête
        payload = {
            "model": "llama2",  # Remplacez par le modèle configuré dans Ollama
            "prompt": f"{system_prompt}\n{self._format_context()}",
        }

        # Envoyer une requête POST à l'API locale d'Ollama
        try:
            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            assistant_response = response.json()["response"]

            # Ajouter la réponse de l'assistant au contexte
            self.context.append({"role": "assistant", "content": assistant_response})

            return assistant_response
        except requests.exceptions.RequestException as e:
            return f"Erreur lors de la communication avec Ollama : {e}"

    def _format_context(self):
        """
        Formater le contexte pour le modèle.
        """
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.context])

    def reset_context(self):
        """
        Réinitialisation du contexte conversationnel.
        """
        self.context = []
