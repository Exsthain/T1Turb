#Alterações nos casos:

    ##GT1 
    
        turbulent_planar

            Casos kE | kO

            High Re Wall Functions | No Wall Functions

            High turbulence intensity | Low turbulence intensity

        turbulent_wedge

            A fazer para Comparação com o GT1 - planar

        Falta

            Unificar gráficos de perfil de camada limite

            Criar gráficos u+/y+ para comparação entre os casos

        Utilização: 
            
            Na pasta GT1/turbulent_planar, rodar o script "run_turbulent_planar.sh", que todos os casos e salva o tempo de execução em um log.


    A FAZER P/ OUTROS CASOS:
    
    ##GT2 - Calcular cf(x), u+, y+, custo computacional e estabilidade numerica dos casos

    Fazer ajuste de intensidade turbulenta?
    Fazer ajuste de malhas(nasa grid 1/2)?

    - Modelos de turbulência com BC certas

    KEpsilon_highRE_v1
        KEpsilon using wall functions
        Right BC values

    KEpsilon_LaunderSharma_V1
        KEpsilon by Launder-Sharma 
        This variant is wall resolving
        Right BC values

    KEpsilon_realizable_highRE
        KEpsilon realizable
        This is a variant of the standard KEpsilon so still has the same limitations
        Right BC values 
        Results not good as expected but tends to do a better job

    
    KOmegaSST_highRE
        KOmega SST - Wall modeling
        Right BC values 

    KOmegaSST_lowRE_v1
        KOmega SST - Wall resolving
        Right BC values 

    no_TM
	    No turbulence model in use

    SA_LRN
        Spalart-Allmaras wall resolving
        Right BC values - nutUSpaldingWallFunction


    DES_KO_HRN
	    DES KOmegaSST wall modeling



    DES_KO_LRN
        DES KOmegaSST wall resolving



    DES_SA_LRN
        DES Spalart-Allmaras wall resolving




    LES-WALE_HRN
	    LES WALE mall modeling



    LES-WALE_LRN
        LES WALE mall Resolving

    (*All LES the results are not accurate because LES requires fine meshes and 3D domains)


    ##GT3 
    - Achar transição por cf(x), crescimento de nut, ou mudança de perfil de velocidade.

    Discutir BC (TU, escalas turbulentas).

    Explicar pq modelo de transição exige abordagem wall resolving.



    Transição:

        Kkl 

        SST-LM

    RANS (Todos wall resolving):

        KOmegaSST v1 - noWF

        kOmegaSST v2 - wall functions

        rKe - wall functions

        RNGkE - wall functions

        Spalart-Allmaras - wall functions

    LES:

        WALE

        Smagorinsky

 

