% IGMS configuration script. Trailing underscores are to minimize bashing
% other festiv variables.

%% Customize the run via the following variables
%--IGMS Simulation Setup
% start timestamp
%start_time_ = '2020-06-01 00:00:00';  
time_file_ = 'MODEL_RULES/time.config';

% transmission constraints
enforce_trans_constraints_ = 1;

% Configure IGMS RTSCED load forecast mode. Options:
%   'festiv_default'  Uses FESTIV's native forecast options. ('' also works)
%   'persist'  Capture IGMS distribution results as persistance forecast
% NOTE: FESTIV's default persistance does not actually use a "real"
% persistance since it is setup from FESTIV timeseries inputs, not the IGMS
% distribution results.
forecast_RTSCED_load_mode_ = 'persist';

%--Provide for load scaling
% Scale run-time "actual" loads. This will be applied to the raw IGMS_core 
% load during the pre-AGC update
%  PJM_5Bus: updated based on igms issue #704
IGMS_load_scale_ = 16.667;

% Scale forecast values, used by DASCUC, RTSCUC, and RTSCED (if no persistance)
%  PJM_5Bus: Note, latest data includes the 20.6 scaling from igms issue #704)
IGMS_input_scale_ = 1;

% Scale reserve values, used by DASCUC, RTSCUC, and RTSCED
%  PJM_5Bus: Note, latest data includes the 20.6 scaling from igms issue #704)
IGMS_reserve_scale_ = 1;


%--AC Powerflow (MATPOWER) setup
% Clean-up parameters for messy powerflow cases
pf_remove_par_lines_ = 0;
pf_imped_scale_ = 1; %0 or 1 = no scaling
pf_alg_ = 3; %0=default 1=Newton-Raphson (default), 2&3=fast decoupled load-flow
pf_max_iter_ = 100; %0=default. Defaults to 10 for Newton and 30 for decoupll=

%--Debugging
% debug mode?  will print various hints from IGMS model rules.
debug_ = 1;

% For interactive session debugging enable the following. Don't use when
% submitting IGMS as a job (comment out by default)
%dbstop if error

% debug powerflow? shows MATPOWER verbose output. Valid values from 0-3
debug_pf_ = 0;

% save powerflow input to file (for offline debugging) at each iteration
% set to '' to skip saving this info
pf_input_savefile_ = 'OUTPUT/pf_in';

% dummy mode? if 1, call a simple script to "communicate" with festiv,
% no zmq server or client is needed.  if 0, requires a zmq server to be
% listening for festiv client.
dummy_ = 0;

%-- Output configuration
% hdf5 file name (will appear in outdir_ directory defined below)
h5name_  = 'igms.h5';    % this file will appear in outdir

% update saved MATLAB workspace at every realtime UC, rather than only at end 
savews_every_RTSCUC_ = true;

% save workspace file at end?  set to '' for no, otherwise specify file.
savews_ = 'igms.mat';

%% Should not need to modify the following variables
% tpc socket for zeromq
socket_ = 'tcp://localhost:5556';

% automatically configure model rules?
auto_model_rules_ = 1;

% paths to required libraries
matpower_ = '/projects/igms/matpower';   % path to matpower   
jsonlab_  = '/projects/igms/festiv/jsonlab';      % path to jsonlab

% output
outdir_   = '../output';     % output directory relative to FESTIV root dir
chunk_    = 128;          % chunksize of extensible direction in arrays
