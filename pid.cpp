#define D_SMOOTHING 3

int p_array[D_SMOOTHING];
int d_pointer = 0;

int get_next_d_pointer ( int current_d_pointer )
{
  return (current_d_pointer + 1) % D_SMOOTHING;
}

void init(void)
{
  for (int x = 0; x < D_SMOOTHING; x++)
    p_array[x] = 0;
}

int get_force_demand(int position, int target, int stiffness) 
{
  return (target - position)*stiffness;
}



void main(void)
{
  int position = get_position();
  int force = get_force();
  int target_force = get_target_force(position, target_position, stiffness);
  
  int p = position - target;
  p_array[d_pointer] = p;
  int next_d_pointer = get_next_d_pointer(d_pointer);
  int d = p_array[next_d_pointer] = p_array[p_pointer];
  int i += p;
  
  if (i_coeficient)
    {
      if (i > i_max)        i = i_max;
      else if (i < -i_max)  i = -i_max;
      
      if (i > 0)
	{
	  if (i > i_decay)  i -= i_decay;
	  else              i  = 0;
	}
      else if (i > 0)
	{
	  if (i < -i_decay) i += i_decay;
	  else              i  = 0;
	}
    }
  output = p * p_coeficient + d * d_coefficient + i * i_coeficient;
}
