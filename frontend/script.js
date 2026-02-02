const API_URL = 'http://localhost:5000/api';

class FreelanceRadar {
    constructor() {
        this.todasAsVagas = [];
        this.vagasFiltradas = [];
        this.currentPage = 1;
        this.perPage = 12;
        this.inicializar();
    }

    inicializar() {
        this.elementos = {
            container: document.getElementById('vagas-container'),
            busca: document.getElementById('busca'),
            filtroPlataforma: document.getElementById('filtroPlataforma'),
            btnLimpar: document.getElementById('btnLimpar'),
            spinner: document.getElementById('spinner')
        };

        this.carregarVagas();
        this.configurarEventos();
    }

    configurarEventos() {
        this.elementos.busca.addEventListener('input', () => this.filtrar());
        this.elementos.filtroPlataforma.addEventListener('change', () => this.filtrar());
        this.elementos.btnLimpar.addEventListener('click', () => this.limparFiltros());
    }

    async carregarVagas() {
        try {
            const response = await fetch(`${API_URL}/vagas`);
            const data = await response.json();
            
            if (!data.sucesso) {
                throw new Error(data.erro || 'Erro ao carregar vagas');
            }

            this.todasAsVagas = data.vagas;
            this.vagasFiltradas = data.vagas;
            this.exibir();

        } catch (error) {
            console.error('Erro:', error);
            this.mostrarErro('Erro ao carregar as vagas. Verifique se o backend está rodando.');
        }
    }

    filtrar() {
        const textoBusca = this.elementos.busca.value.toLowerCase();
        const plataforma = this.elementos.filtroPlataforma.value;

        this.vagasFiltradas = this.todasAsVagas.filter(vaga => {
            const matchBusca = 
                vaga.titulo.toLowerCase().includes(textoBusca) ||
                vaga.descricao.toLowerCase().includes(textoBusca);
            
            const matchPlataforma = !plataforma || vaga.plataforma === plataforma;

            return matchBusca && matchPlataforma;
        });

        this.currentPage = 1;
        this.exibir();
    }

    exibir() {
        if (this.vagasFiltradas.length === 0) {
            this.mostrarVazio();
            return;
        }

        const inicio = (this.currentPage - 1) * this.perPage;
        const fim = inicio + this.perPage;
        const vagas = this.vagasFiltradas.slice(inicio, fim);

        this.elementos.container.innerHTML = vagas.map(vaga => this.criarCard(vaga)).join('');
    }

    criarCard(vaga) {
        const habilidades = vaga.habilidades ? vaga.habilidades.split(',') : [];
        const tagsHtml = habilidades.length > 0 
            ? habilidades.map(h => `<span class="tag">${h.trim()}</span>`).join('')
            : '';

        return `
            <div class="col-12 col-sm-6 col-lg-4">
                <div class="vaga-card">
                    <span class="vaga-plataforma">${vaga.plataforma}</span>
                    <h5 class="vaga-titulo">${vaga.titulo}</h5>
                    <p class="vaga-preco">💰 ${vaga.preco}</p>
                    <p class="vaga-descricao">${vaga.descricao}</p>
                    ${tagsHtml ? `<div class="tags-container">${tagsHtml}</div>` : ''}
                    <p class="vaga-data">📅 ${this.formatarData(vaga.data)}</p>
                </div>
            </div>
        `;
    }

    formatarData(data) {
        return new Date(data).toLocaleDateString('pt-BR');
    }

    limparFiltros() {
        this.elementos.busca.value = '';
        this.elementos.filtroPlataforma.value = '';
        this.vagasFiltradas = this.todasAsVagas;
        this.currentPage = 1;
        this.exibir();
    }

    mostrarVazio() {
        this.elementos.container.innerHTML = `
            <div class="col-12">
                <p class="text-center text-muted py-5">
                    🔍 Nenhuma vaga encontrada com esses filtros.
                </p>
            </div>
        `;
    }

    mostrarErro(mensagem) {
        this.elementos.container.innerHTML = `
            <div class="col-12">
                <p class="text-center text-danger py-5">⚠️ ${mensagem}</p>
            </div>
        `;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new FreelanceRadar();
});