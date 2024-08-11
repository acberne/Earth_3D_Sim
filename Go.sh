cwd=$(pwd)




####0
yes | cp -rf arr_0.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py




####1
yes | cp -rf arr_1.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py


####2
yes | cp -rf arr_2.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py



####3
yes | cp -rf arr_3.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py



####4
yes | cp -rf arr_4.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py



####5
yes | cp -rf arr_5.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py



####6
yes | cp -rf arr_6.npy arr_inp.npy
python Read.py ##Make 0 preturbation of interior structure and copy file
yes | cp -rf ct1.dat $cwd/Tidal_Response/model
yes | cp -rf ct1_spectrum_enh.dat $cwd/Tidal_Response/model

cd $cwd/Tidal_Response ##Running Preturbaion Code
matlab -nodisplay -nodesktop -r "run tidal_response_30.m;exit" #Getting 3 baseline response
matlab -nodisplay -nodesktop -r "run tidal_response_20.m;exit" #Getting 20 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_21.m;exit" #Getting 21 + Couplings
matlab -nodisplay -nodesktop -r "run tidal_response_22.m;exit" #Getting 22 + Couplings
cd $cwd

##Getting Love Numbers
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD20.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD21.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD22.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD30.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD31.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD32.dat $cwd
yes | cp -rf $cwd/Tidal_Response/resp/resp.MCMC_response_TD33.dat $cwd

python kaula-fg.py ##Get functions describing relative potentials
python Get_h2.py
python Get_20.py
python Get_21.py
python Get_22.py
python Get_30.py
python Get_31.py #FIX THESE
python Get_32.py
python Get_33.py




