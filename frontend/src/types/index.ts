export interface MenuRoute {
	path: string;
	title?: string;
	name?: string;
	icon?: | string | { render: () => void };
	redirect?: string;
	children: MenuRoute[];
	meta: any
}

export type UserInfo = {
	userName: string,
	signature: string,
	userId: string,
	sex: string,
	email: string,
	avatar: string
}

export type UserAvatarList = {
	userHistoryFileList: Array<string>,
	systemAvatarList: Array<string>
};

export type ProjectType = {
	_id: string,
	name: string,
	status: string,
	create_time: string,
	crash_num: number,
	seed_num: number,
	container_id: string,
	user_id: string,
	binary_path: string,
	binary_cov_path: string,
	output_path: string,
	input_path: string,
	binary_args: string,
	target_path: string
};

export type ContainerType = {
	_id: string,
	name: string,
	status: string,
	create_time: string,
	ssh_port: number,
	ws_port: number,
	container_id: string,
	user_id: string,
	ssh_host: string,
	ws_host: string
};

export type FuzzStatType = {
	run_time: string,
	cycles_done: string,
	last_new_path: string,
	total_path: string,
	last_uniq_crash: string,
	uniq_crashes: string,
	last_uniq_hang: string,
	uniq_hangs: string,
	now_processing: string,
	map_density: string,
	paths_timed_out: string,
	count_coverage: string,
	now_trying: string,
	favored_paths: string,
	stage_execs: string,
	new_edges_on: string,
	total_execs: string,
	total_crashes: string,
	exec_speed: string,
	total_tmouts: string,
	bit_flips: string,
	levels: string,
	byte_flips: string,
	pending: string,
	arithmetics: string,
	pend_fav: string,
	known_inis: string,
	own_finds: string,
	dictionary: string,
	imported: string,
	havoc: string,
	stability: string,
	trim: string,
	cpu: string,
};

export type QueueEntryType = {
	fname: string,
	len: number,
	cal_failed: number,
	trim_done: number,
	was_fuzzed: number,
	passed_det: number,
	has_new_cov: number,
	favored: number,
	fs_redundant: number,
	exec_us: number,
	handicap: number,
	depth: number,
	distance: number,
	perf_score: number,
	user_set_perf_score: number,
	target_coverage_score: number,
	queue_idx: number
};