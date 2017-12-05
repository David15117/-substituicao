from rest_framework import routers, serializers, viewsets
from transporte.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')
class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('__all__')
class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ('__all__')
class MotoristaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motorista
        fields = ('__all__')
class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    	#usuario = UserSerializer(many=False)
	class Meta:
		model = Funcionario
		fields = ('__all__')
	def create(self,dados):
		dados_user=dados.pop('usuario')# remove usuario
		u = User.objects.create(**dados_user)# criar o usuario
		p = Funcionario.objects.create(usuario=u,**dados)#criar pessoa, e em dados insere objetivo de usuario
		return p
class DepartamentoSocitacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DepartamentoSocitacao
        fields = ('__all__')
class AtenderSolicitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AtenderSolicita
        fields = ('__all__')